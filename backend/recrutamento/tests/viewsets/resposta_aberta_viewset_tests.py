from model_bakery import baker

from recrutamento.models import RespostaAberta

from .base_viewset_test import BaseViewsetTest


class TestRespostaAbertaViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de RespostaAberta.
    """

    app = "recrutamento"
    model = RespostaAberta
    model_name = "resposta_aberta"
    url_name_list = "respostas-abertas-list"
    url_name_detail = "respostas-abertas-detail"
    allowed_methods = ["GET", "POST", "HEAD", "OPTIONS"]

    def setUp(self):
        self.candidato = baker.make("recrutamento.Candidato")
        self.pergunta_aberta = baker.make("recrutamento.PerguntaAberta")

        self.valid_payload = {
            "candidato": self.candidato.id,
            "pergunta_aberta": self.pergunta_aberta.id,
            "resposta": "Teste",
        }

        super().setUp()
