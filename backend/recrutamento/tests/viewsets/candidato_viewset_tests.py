from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from model_bakery import baker

from recrutamento.models import Candidato

from .base_viewset_test import BaseViewsetTest


class TestCandidatoViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de Candidato.
    """

    app = "recrutamento"
    model = Candidato
    model_name = "candidato"
    url_name_list = "candidatos-list"
    url_name_detail = "candidatos-detail"
    allowed_methods = ["GET", "POST", "HEAD", "OPTIONS"]

    def setUp(self):
        file = SimpleUploadedFile("file.txt", b"0" * 1024 * 100)
        self.vaga = baker.make("recrutamento.Vaga")
        self.pergunta_aberta = baker.make("recrutamento.PerguntaAberta", vaga=self.vaga)
        self.instituicao = baker.make("recrutamento.Instituicao")
        self.curso = baker.make("recrutamento.Curso")
        self.skill = baker.make("recrutamento.Skill")

        self.valid_payload = {
            "nome": "Candidato Teste",
            "vaga": self.vaga.id,
            "data_nascimento": "2000-01-01",
            "sobre_mim": "Descrição da candidato teste",
            "estado": "RN",
            "email": "candidato@novadata.com.br",
            "whatsapp": "84999999999",
            "expectativa_2anos": "O céu é o limite",
            "expectativa_10anos": "O universo é o limite",
            "comunicativo": True,
            "ingles": 3,
            "empregado": True,
            "disponibilidade": "IMEDIATA",
            "horarios": "FULL-TIME",
            "pretensao_salarial_pj": 1000.00,
            "pretensao_salarial_clt": 2000.00,
            "curriculo": file,
            "github_portfolio": "https://www.google.com",
            "linkedin": "https://www.google.com",
            "formacao_candidato": [
                {
                    "instituicao": self.instituicao.id,
                    "curso": self.curso.id,
                    "grau": 4,
                    "data_inicio": "2015-01-01",
                    "data_conclusao": "2019-01-01",
                },
                {
                    "instituicao": self.instituicao.id,
                    "curso": self.curso.id,
                    "grau": 6,
                    "data_inicio": "2019-01-01",
                    "data_conclusao": "2021-01-01",
                },
                {
                    "instituicao": self.instituicao.id,
                    "curso": self.curso.id,
                    "grau": 2,
                    "data_inicio": "2022-01-01",
                    "data_conclusao": "2024-01-01",
                },
            ],
            "skill_candidato": [
                {
                    "skill": self.skill.id,
                    "avaliacao": 4,
                    "tempo_experiencia": 2,
                },
                {
                    "skill": self.skill.id,
                    "avaliacao": 3,
                    "tempo_experiencia": 4,
                },
            ],
            "resposta_aberta": [
                {
                    "pergunta_aberta": self.pergunta_aberta.id,
                    "resposta": "Teste de resposta 1",
                },
                {
                    "pergunta_aberta": self.pergunta_aberta.id,
                    "resposta": "Teste de resposta 2",
                },
            ],
        }

        super().setUp()

    def test_create_candidato_with_inlines(self):
        """
        Testa a criação de um candidato.
        """
        url = reverse(self.url_name_list)
        qtd_anterior = Candidato.objects.count()
        response = self.client.post(url, self.valid_payload)
        print(response)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Candidato.objects.count(), qtd_anterior + 1)
        self.assertEqual(Candidato.objects.last().skillcandidato_set.count(), 2)
        self.assertEqual(Candidato.objects.last().formacaocandidato_set.count(), 3)
        self.assertEqual(Candidato.objects.last().respostaaberta_set.count(), 2)
