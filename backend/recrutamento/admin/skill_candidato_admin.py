from unfold.admin import TabularInline

from ..models import SkillCandidato


class SkillCandidatoInline(TabularInline):
    model = SkillCandidato

    extra = 0

    autocomplete_fields = ['skill']
