from model_bakery import baker

from recrutamento.admin.vaga_admin import VagaAdmin
from recrutamento.models import Vaga

from .base_admin_test import BaseAdminTest


class VagaAdminTest(BaseAdminTest):
    admin_class = VagaAdmin
    app = "recrutamento"
    model = Vaga
    model_name = "vaga"

    def setUp(self):
        super().setUp()
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
            "beneficios": [],
            "requisitos": [],
            "diferenciais": [],
            "perguntaaberta_set-TOTAL_FORMS": "0",  # Nenhum formulário enviado
            "perguntaaberta_set-INITIAL_FORMS": "0",  # Nenhum formulário existente
            "perguntaaberta_set-MIN_NUM_FORMS": "0",  # Número mínimo de formulários
            "perguntaaberta_set-MAX_NUM_FORMS": "1000",
        }
