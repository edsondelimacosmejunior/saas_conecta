from model_bakery import baker

from recrutamento.models import PerguntaAberta

from .base_viewset_test import BaseViewsetTest


class TestPerguntaAbertaViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de PerguntaAberta.
    """

    app = "recrutamento"
    model = PerguntaAberta
    model_name = "pergunta_aberta"
    url_name_list = "perguntas-abertas-list"
    url_name_detail = "perguntas-abertas-detail"
    allowed_methods = ["GET", "HEAD", "OPTIONS"]

    def setUp(self):
        self.vaga = baker.make("recrutamento.Vaga")

        self.valid_payload = {
            "titulo": "Pergunta Aberta Teste",
            "vaga": self.vaga.id,
            "obrigatorio": True,
        }
        super().setUp()
