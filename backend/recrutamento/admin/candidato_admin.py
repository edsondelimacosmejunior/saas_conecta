from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import Candidato
from .formacao_candidato_admin import FormacaoCandidatoInline
from .resposta_aberta_admin import RespostaAbertaInline
from .resposta_candidato_skill_diferencial_admin import \
    RepostaCandidatoSkillDiferencialInline
from .skill_candidato_admin import SkillCandidatoInline


@admin.register(Candidato)
class CandidatoAdmin(ModelAdmin):
    list_display = [
        "id",
        "nome",
        "vaga",
        "email",
        "whatsapp",
        "estado",
        "pretensao_salarial_pj",
        "pretensao_salarial_clt",
        "empregado",
        "disponibilidade",
    ]

    search_fields = ["nome"]

    list_filter = [
        "vaga",
        "estado",
        "ingles",
        "empregado",
        "disponibilidade",
        "horarios",
        "comunicativo",
    ]

    autocomplete_fields = [
        "vaga",
    ]

    list_filter = [
        "vaga",
        "usuario_criacao",
        "usuario_atualizacao",
    ]

    readonly_fields = [
        "data_criacao",
        "data_atualizacao",
        "usuario_criacao",
        "usuario_atualizacao",
    ]

    inlines = [
        RepostaCandidatoSkillDiferencialInline,
        FormacaoCandidatoInline,
        SkillCandidatoInline,
        RespostaAbertaInline,
    ]

    fieldsets = [
        (
            "Dados Pessoais",
            {
                "fields": [
                    "vaga",
                    "nome",
                    "data_nascimento",
                    "cpf",
                    "sobre_mim",
                    "estado",
                ]
            },
        ),
        (
            "Contatos",
            {
                "fields": [
                    "email",
                    "whatsapp",
                ]
            },
        ),
        (
            "Expectativa Profissional",
            {
                "fields": [
                    "expectativa_2anos",
                    "expectativa_10anos",
                ]
            },
        ),
        (
            "Principais Skills",
            {
                "fields": [
                    "comunicativo",
                    "ingles",
                ]
            },
        ),
        (
            "Dados Profissionais",
            {
                "fields": [
                    "empregado",
                    "disponibilidade",
                    "horarios",
                    "pretensao_salarial_pj",
                    "pretensao_salarial_clt",
                    "curriculo",
                    "resposta_vaga_generica",
                    "github_portfolio",
                    "linkedin",
                    "indicacao",
                ]
            },
        ),
        (
            "Teste Técnico",
            {
                "fields": [
                    "teste_tecnico",
                    "link_teste_tecnico",
                ]
            },
        ),

        ("Diferenciais", {
            "fields": ["interesse_diferenciais"],
        }),

        (
            "Dados Adicionais",
            {
                "classes": ("collapse",),
                "fields": [
                    "data_criacao",
                    "data_atualizacao",
                    "usuario_criacao",
                    "usuario_atualizacao",
                ],
            },
        ),
    ]
