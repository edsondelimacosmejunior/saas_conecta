from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import Vaga
from .pergunta_aberta_admin import PerguntaAbertaInline
from .peso_skill_inline import PesoSkillInline

@admin.register(Vaga)
class VagaAdmin(ModelAdmin):
    list_display = [
        "id",
        "titulo",
        "area_atuacao",
        "ativa",
    ]

    search_fields = ["titulo"]

    autocomplete_fields = [
        "area_atuacao",
    ]

    readonly_fields = [
        "data_criacao",
        "data_atualizacao",
        "usuario_criacao",
        "usuario_atualizacao",
    ]

    filter_horizontal = [
        "beneficios",
        "requisitos",
        "diferenciais",
    ]

    inlines = [
        PesoSkillInline,
        PerguntaAbertaInline,
    ]

    list_filter = [
        "ativa",
        "tipo_regime_trabalho",
        "tipo_contratacao",
        "area_atuacao",
        "usuario_criacao",
        "usuario_atualizacao",
    ]

    fieldsets = [
        (
            "Dados Principais",
            {
                "fields": [
                    "titulo",
                    "slug",
                    "sobre",
                    "responsabilidades",
                    "data_fechamento",
                    "ativa",
                ]
            },
        ),
        (
            "Regime de Contratação",
            {
                "fields": [
                    "salario",
                    "tipo_regime_trabalho",
                    "area_atuacao",
                    "tipo_contratacao",
                    "vaga_generica",
                    "beneficios",
                ]
            },
        ),
        (
            "Requisitos & Diferenciais",
            {
                "fields": [
                    "requisitos",
                    "diferenciais",
                ]
            },
        ),
        (
            "Teste Técnico",
            {
                "fields": [
                    "teste_tecnico",
                ]
            },
        ),
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
