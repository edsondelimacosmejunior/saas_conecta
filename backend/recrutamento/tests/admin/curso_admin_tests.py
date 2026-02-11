from recrutamento.admin.curso_admin import CursoAdmin
from recrutamento.models import Curso

from .base_admin_test import BaseAdminTest


class CursoAdminTest(BaseAdminTest):
    admin_class = CursoAdmin
    app = "recrutamento"
    model = Curso
    model_name = "curso"

    def setUp(self):
        super().setUp()

        self.valid_payload = {
            "nome": "Curso Teste",
            "descricao": "curso-teste",
        }
