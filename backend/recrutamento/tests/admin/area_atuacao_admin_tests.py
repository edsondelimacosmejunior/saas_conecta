from recrutamento.admin.area_atuacao_admin import AreaAtuacaoAdmin
from recrutamento.models import AreaAtuacao

from .base_admin_test import BaseAdminTest


class AreaAtuacaoAdminTest(BaseAdminTest):
    admin_class = AreaAtuacaoAdmin
    app = "recrutamento"
    model = AreaAtuacao
    model_name = "areaatuacao"

    def setUp(self):
        super().setUp()

        self.valid_payload = {
            "nome": "Área de Atuação Teste",
            "descricao": "area-atuacao-teste",
        }
