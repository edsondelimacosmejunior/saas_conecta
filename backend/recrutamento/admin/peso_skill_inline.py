from ..models import PesoSkill
from unfold.admin import TabularInline

class PesoSkillInline(TabularInline):
    model = PesoSkill

    extra = 0
    autocomplete_fields = [
        'skill'
    ]
    readonly_fields = [
        'data_criacao',
        'data_atualizacao',
        'usuario_criacao',
        'usuario_atualizacao',
    ]