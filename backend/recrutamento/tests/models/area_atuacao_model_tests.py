from recrutamento.models import AreaAtuacao

from .base_model_test import BaseModelTest


class AreaAtuacaoModelTest(BaseModelTest):
    model = AreaAtuacao
    app = "recrutamento"
    model_name = "area_atuacao"
    valid_payload = {
        "nome": "Área de Atuação Teste",
        "descricao": "area-atuacao-teste",
    }
