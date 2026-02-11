from unfold.admin import TabularInline

from ..models import RespostaAberta


class RespostaAbertaInline(TabularInline):
    model = RespostaAberta

    extra = 0

    readonly_fields = ["pergunta_aberta"]
