from unfold.admin import TabularInline

from ..models import FormacaoCandidato


class FormacaoCandidatoInline(TabularInline):
    model = FormacaoCandidato

    extra = 0

    autocomplete_fields = ['curso', 'instituicao']
