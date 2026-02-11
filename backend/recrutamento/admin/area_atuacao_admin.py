from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import AreaAtuacao


@admin.register(AreaAtuacao)
class AreaAtuacaoAdmin(ModelAdmin):
    list_display = ["id", "nome"]

    search_fields = ["nome"]

    readonly_fields = [
        "data_criacao",
        "data_atualizacao",
        "usuario_criacao",
        "usuario_atualizacao",
    ]

    list_filter = ["usuario_criacao", "usuario_atualizacao"]

    fieldsets = [
        (
            "Dados Principais",
            {
                "fields": [
                    "nome",
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
