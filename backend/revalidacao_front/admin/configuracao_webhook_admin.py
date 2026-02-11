from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import ConfiguracaoWebhook
from .configuracao_signals_admin import ConfiguracaoSignalInline


@admin.register(ConfiguracaoWebhook)
class ConfiguracaoWebhookAdmin(ModelAdmin):
    list_display = ["id", "nome", "ativa"]

    search_fields = ["nome"]

    list_filter = ["ativa"]

    readonly_fields = [
        "data_criacao",
        "data_atualizacao",
        "usuario_criacao",
        "usuario_atualizacao",
    ]

    inlines = [ConfiguracaoSignalInline]

    fieldsets = [
        (
            "Dados Principais",
            {
                "fields": [
                    "nome",
                    "url",
                    "ativa",
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
