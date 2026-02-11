from model_bakery import baker

from recrutamento.models import PerguntaAberta

from .base_model_test import BaseModelTest


class PerguntaAbertaModelTest(BaseModelTest):
    model = PerguntaAberta
    app = "recrutamento"
    model_name = "pergunta_aberta"

    def setUp(self):
        self.vaga = baker.make("recrutamento.Vaga")

        self.valid_payload = {
            "titulo": "Pergunta Aberta Teste",
            "vaga": self.vaga,
            "obrigatorio": True,
        }
        super().setUp()
