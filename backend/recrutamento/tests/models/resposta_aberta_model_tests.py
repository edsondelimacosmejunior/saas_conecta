from model_bakery import baker

from recrutamento.models import RespostaAberta

from .base_model_test import BaseModelTest


class RespostaAbertaModelTest(BaseModelTest):
    model = RespostaAberta
    app = "recrutamento"
    model_name = "resposta_aberta"

    def setUp(self):
        self.candidato = baker.make("recrutamento.Candidato")
        self.pergunta_aberta = baker.make("recrutamento.PerguntaAberta")

        self.valid_payload = {
            "candidato": self.candidato,
            "pergunta_aberta": self.pergunta_aberta,
            "resposta": "Teste",
        }

        super().setUp()
