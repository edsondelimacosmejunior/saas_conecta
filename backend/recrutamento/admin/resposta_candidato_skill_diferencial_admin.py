from django.contrib import admin
from recrutamento.models.resposta_candidato_skill_diferencial import \
    RepostaCandidatoSkillDiferencial
from unfold.admin import ModelAdmin, TabularInline


@admin.register(RepostaCandidatoSkillDiferencial)
class RepostaCandidatoSkillDiferencialAdmin(ModelAdmin):
    list_display = [
        'id',
        'candidato',
        'skill',
        'resposta',
        'data_criacao',
        'data_atualizacao',
        'usuario_criacao',
        'usuario_atualizacao',
    ]

    search_fields = [
        'id',
        'candidato__nome',
        'skill__nome',
    ]

    list_filter = [
        'candidato',
        'skill',
        'data_criacao',
        'data_atualizacao',
        'usuario_criacao',
        'usuario_atualizacao',
    ]

    list_select_related = [
        'candidato',
        'skill',
    ]

    autocomplete_fields = [
        'candidato',
        'skill',
    ]
    readonly_fields = [
        'data_criacao',
        'data_atualizacao',
        'usuario_criacao',
        'usuario_atualizacao',
    ]

class RepostaCandidatoSkillDiferencialInline(TabularInline):
    model = RepostaCandidatoSkillDiferencial
    extra = 0
    autocomplete_fields = ['candidato', 'skill']
    verbose_name = "skill Diferencial"
    verbose_name_plural = "skills Diferenciais"
