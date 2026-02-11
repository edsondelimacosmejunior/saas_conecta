from recrutamento.models import Instituicao

from .base_model_test import BaseModelTest


class InstituicaoModelTest(BaseModelTest):
    model = Instituicao
    required_fields = ["nome"]
    app = "recrutamento"
    model_name = "instituicao"
    valid_payload = {
        "nome": "Instituicao Teste",
    }
