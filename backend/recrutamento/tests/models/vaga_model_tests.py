from model_bakery import baker

from recrutamento.models import Vaga

from .base_model_test import BaseModelTest


class VagaModelTest(BaseModelTest):
    model = Vaga
    required_fields = ["nome"]
    app = "recrutamento"
    model_name = "vaga"
    valid_payload = {
        "nome": "Área de Atuação Teste",
        "descricao": "area-atuacao-teste",
    }

    def setUp(self):
        self.area_atuacao = baker.make("recrutamento.AreaAtuacao")

        self.valid_payload = {
            "titulo": "Vaga Teste",
            "slug": "vaga-teste",
            "sobre": "Descrição da vaga teste",
            "responsabilidades": "Responsabilidades da vaga teste",
            "data_fechamento": "2022-12-31",
            "ativa": True,
            "salario": 1000.00,
            "tipo_regime_trabalho": "PRESENCIAL",
            "area_atuacao": self.area_atuacao,
            "tipo_contratacao": "CLT",
        }

        super().setUp()
