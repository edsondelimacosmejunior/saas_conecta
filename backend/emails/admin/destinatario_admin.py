from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import Destinatario


@admin.register(Destinatario)
class DestinatarioAdmin(ModelAdmin):
    list_display = [
        'id',
        'email'
    ]

    search_fields = [
        'id',
        'email'
    ]