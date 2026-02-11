from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import Skill


@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = [
        "id",
        "nome",
        "tipo",
    ]

    search_fields = ["nome"]

    list_filter = ["tipo", "usuario_criacao", "usuario_atualizacao"]

    readonly_fields = [
        "data_criacao",
        "data_atualizacao",
        "usuario_criacao",
        "usuario_atualizacao",
    ]

    fieldsets = [
        (
            "Dados Principais",
            {
                "fields": [
                    "nome",
                    "tipo",
                    "descricao",
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
