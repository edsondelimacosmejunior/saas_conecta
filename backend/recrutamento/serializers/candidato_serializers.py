import json

from global_functions.utils.parse_json_data import parse_json_data
from global_functions.utils.string_to_dict import transformar_em_dict
from rest_framework import serializers

from ..models import (Candidato, Curso, FormacaoCandidato, Instituicao,
                      PerguntaAberta, RepostaCandidatoSkillDiferencial,
                      RespostaAberta, Skill, SkillCandidato)
from .formacao_candidato_serializers import FormacaoCandidatoSerializer
from .resposta_aberta_serializers import RespostaAbertaSerializer
from .resposta_candidato_skill_diferencial_serializers import \
    RepostaCandidatoSkillDiferencialSerializer
from .skill_candidato_serializers import SkillCandidatoSerializer


class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = "__all__"


class CandidatoCreateSerializer(serializers.ModelSerializer):
    formacao_candidato = FormacaoCandidatoSerializer(
        many=True, required=False, source="formacaocandidato_set"
    )
    skill_candidato = SkillCandidatoSerializer(
        many=True, required=False, source="skillcandidato_set"
    )
    resposta_aberta = RespostaAbertaSerializer(
        many=True, required=False, source="respostaaberta_set"
    )

    resposta_diferencial = RepostaCandidatoSkillDiferencialSerializer(
        many=True, required=False, source="diferenciais"
    )

    def create(self, validated_data):
        formacoes_data = parse_json_data(
            self.initial_data.pop("formacao_candidato", "[]")
        )
        skills_data = parse_json_data(self.initial_data.pop("skill_candidato", "[]"))
        respostas_data = parse_json_data(self.initial_data.pop("resposta_aberta", "[]"))

        respostas_diferencial_data = parse_json_data(
            self.initial_data.pop("resposta_diferencial", "[]")
        )

        # Cria o candidato principal
        candidato = Candidato.objects.create(**validated_data)

        # Cria as formações relacionadas
        self._criar_formacoes(candidato, formacoes_data)

        # Cria as skills relacionadas
        self._criar_skills(candidato, skills_data)

        # Cria as respostas relacionadas
        self._criar_respostas(candidato, respostas_data)

        self._criar_respostas_diferenciais(candidato, respostas_diferencial_data)

        return candidato

    def _criar_formacoes(self, candidato, formacoes_data):
        for formacao in formacoes_data:
            formacao = transformar_em_dict(formacao)
            instituicao_id = formacao.pop("instituicao", None)
            curso_id = formacao.pop("curso", None)

            if not instituicao_id or not curso_id:
                raise serializers.ValidationError(
                    "Instituição e curso são obrigatórios para criar uma formação."
                )

            try:
                instituicao = Instituicao.objects.get(pk=instituicao_id)
                curso = Curso.objects.get(pk=curso_id)
            except (Instituicao.DoesNotExist, Curso.DoesNotExist) as e:
                raise serializers.ValidationError(
                    f"Erro ao buscar instituição ou curso: {e}"
                )

            FormacaoCandidato.objects.create(
                candidato=candidato, instituicao=instituicao, curso=curso, **formacao
            )

    def _criar_skills(self, candidato, skills_data):
        for skill_candidato in skills_data:
            skill_candidato = transformar_em_dict(skill_candidato)
            skill_id = skill_candidato.pop("skill", None)

            if not skill_id:
                raise serializers.ValidationError(
                    "Skill é obrigatória para criar uma habilidade."
                )

            try:
                skill = Skill.objects.get(pk=skill_id)
            except Skill.DoesNotExist as e:
                raise serializers.ValidationError(f"Erro ao buscar skill: {e}")

            SkillCandidato.objects.create(
                candidato=candidato, skill=skill, **skill_candidato
            )

    def _criar_respostas(self, candidato, respostas_data):
        for resposta_candidato in respostas_data:
            resposta_candidato = transformar_em_dict(resposta_candidato)
            pergunta_aberta_id = resposta_candidato.pop("pergunta_aberta", None)

            if not pergunta_aberta_id:
                raise serializers.ValidationError(
                    "Pergunta aberta é obrigatória para criar uma resposta."
                )

            try:
                pergunta_aberta = PerguntaAberta.objects.get(pk=pergunta_aberta_id)
            except PerguntaAberta.DoesNotExist as e:
                raise serializers.ValidationError(
                    f"Erro ao buscar pergunta aberta: {e}"
                )

            RespostaAberta.objects.create(
                candidato=candidato,
                pergunta_aberta=pergunta_aberta,
                **resposta_candidato,
            )

    def _criar_respostas_diferenciais(self, candidato, respostas_diferencial_data):
        for item in respostas_diferencial_data:
            data = transformar_em_dict(item)
            skill_id = data.pop("skill", None)
            if not skill_id:
                raise serializers.ValidationError(
                    "Skill é obrigatória para criar a resposta de diferencial."
                )
            try:
                skill = Skill.objects.get(pk=skill_id)
            except Skill.DoesNotExist as e:
                raise serializers.ValidationError(f"Erro ao buscar skill: {e}")

            resposta_val = data.get("resposta", None)

            RepostaCandidatoSkillDiferencial.objects.create(
                candidato=candidato,
                skill=skill,
                resposta=resposta_val,
            )

    class Meta:
        model = Candidato
        fields = "__all__"
