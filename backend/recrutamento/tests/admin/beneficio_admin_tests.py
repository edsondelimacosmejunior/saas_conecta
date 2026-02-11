from recrutamento.admin.beneficio_admin import BeneficioAdmin
from recrutamento.models import Beneficio

from .base_admin_test import BaseAdminTest


class BeneficioAdminTest(BaseAdminTest):
    admin_class = BeneficioAdmin
    app = "recrutamento"
    model = Beneficio
    model_name = "beneficio"

    def setUp(self):
        super().setUp()

        self.valid_payload = {
            "nome": "Beneficio Teste",
            "descricao": "beneficio-teste",
        }
