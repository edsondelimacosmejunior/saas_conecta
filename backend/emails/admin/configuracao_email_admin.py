from django.contrib import admin
from unfold.admin import ModelAdmin
from ..models import ConfiguracaoEmail


@admin.register(ConfiguracaoEmail)
class ConfiguracaoEmailAdmin(ModelAdmin):
    list_display = ["id","email_backend","email_use_tls"]
    search_fields = ["email_name"]
    readonly_fields = ["data_criacao", "data_atualizacao", "usuario_criacao","usuario_atualizacao"]
