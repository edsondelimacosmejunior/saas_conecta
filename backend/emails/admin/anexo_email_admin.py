from django.contrib import admin
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from import_export.forms import SelectableFieldsExportForm

from ..models import AnexoEmail


@admin.register(AnexoEmail)
class AnexoEmailAdmin(ImportExportModelAdmin, ModelAdmin):
    list_display = [
        "id",
        "nome_interno",
        "anexo",
        "template_email",
    ]

    autocomplete_fields = [
        "template_email",
    ]

    search_fields = [
        "id",
        "nome_interno",
        "template_email__nome_interno",
    ]

    list_filter = [
        "template_email",
    ]

    readonly_fields = [
        "data_criacao",
        "data_atualizacao",
        "usuario_criacao",
        "usuario_atualizacao",
    ]

    fieldsets = [
        (
            "Dados principais",
            {
                "fields": [
                    "nome_interno",
                    "anexo",
                    "template_email",
                ]
            },
        ),
        (
            "Auditoria",
            {
                "fields": [
                    "data_criacao",
                    "data_atualizacao",
                    "usuario_criacao",
                    "usuario_atualizacao",
                ]
            },
        ),
    ]

    export_form_class = SelectableFieldsExportForm