from django.contrib import admin

from ..models import AnexoEmail
from unfold.admin import TabularInline


class AnexoEmailInline(TabularInline):
    model = AnexoEmail

    extra = 0

    exclude = [
        "usuario_criacao",
        "usuario_atualizacao",
    ]