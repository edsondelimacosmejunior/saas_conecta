from django.contrib import admin

from ..models import PesoSkill


@admin.register(PesoSkill)
class PesoSkillAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'vaga',
        'skill',
        'peso',
    ]

    readonly_fields = [
        'data_criacao',
        'data_atualizacao',
        'usuario_criacao',
        'usuario_atualizacao',
    ]
