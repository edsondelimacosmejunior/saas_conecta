from unfold.admin import TabularInline

from ..models import PerguntaAberta


class PerguntaAbertaInline(TabularInline):
    model = PerguntaAberta

    extra = 0

    readonly_fields = [
        'data_criacao',
        'data_atualizacao',
        'usuario_criacao',
        'usuario_atualizacao',
    ]
