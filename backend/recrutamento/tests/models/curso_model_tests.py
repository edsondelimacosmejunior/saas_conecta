from recrutamento.models import Curso

from .base_model_test import BaseModelTest


class CursoModelTest(BaseModelTest):
    model = Curso
    required_fields = ["nome"]
    app = "recrutamento"
    model_name = "curso"
    valid_payload = {
        "nome": "Curso Teste",
        "descricao": "curso-teste",
    }
