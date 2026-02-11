from django.contrib import admin
from unfold.admin import TabularInline

from ..models import ConfiguracaoSignal


class ConfiguracaoSignalInline(TabularInline):
    model = ConfiguracaoSignal

    extra = 0

    readonly_fields = [
        "data_criacao",
        "data_atualizacao",
        "usuario_criacao",
        "usuario_atualizacao",
    ]
