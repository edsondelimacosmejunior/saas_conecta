from model_bakery import baker

from recrutamento.models import Vaga

from .base_viewset_test import BaseViewsetTest


class TestVagaViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de Vaga.
    """

    app = "recrutamento"
    model = Vaga
    model_name = "vaga"
    url_name_list = "vagas-list"
    url_name_detail = "vagas-detail"
    allowed_methods = ["GET", "HEAD", "OPTIONS"]

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
            "area_atuacao": self.area_atuacao.id,
            "tipo_contratacao": "CLT",
        }

        super().setUp()
