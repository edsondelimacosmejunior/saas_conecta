from django.contrib import admin
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin

from ..models import Instituicao


@admin.register(Instituicao)
class InstituicaoAdmin(ImportExportModelAdmin, ModelAdmin):
    list_display = ["id", "nome"]

    search_fields = ["nome"]

    list_filter = ["usuario_criacao", "usuario_atualizacao"]

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
