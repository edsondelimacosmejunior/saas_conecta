from recrutamento.models import Beneficio

from .base_model_test import BaseModelTest


class BeneficioModelTest(BaseModelTest):
    model = Beneficio
    app = "recrutamento"
    model_name = "beneficio"
    valid_payload = {
        "nome": "Benefício Teste",
        "descricao": "area-atuacao-teste",
    }
