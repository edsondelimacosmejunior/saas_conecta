from django.contrib import admin
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin

from ..models import Curso


@admin.register(Curso)
class CursoAdmin(ImportExportModelAdmin, ModelAdmin):
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
