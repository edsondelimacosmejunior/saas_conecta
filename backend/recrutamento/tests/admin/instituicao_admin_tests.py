from recrutamento.admin.instituicao_admin import InstituicaoAdmin
from recrutamento.models import Instituicao

from .base_admin_test import BaseAdminTest


class InstituicaoAdminTest(BaseAdminTest):
    admin_class = InstituicaoAdmin
    app = "recrutamento"
    model = Instituicao
    model_name = "instituicao"

    def setUp(self):
        super().setUp()

        self.valid_payload = {
            "nome": "Instituicao Teste",
        }
