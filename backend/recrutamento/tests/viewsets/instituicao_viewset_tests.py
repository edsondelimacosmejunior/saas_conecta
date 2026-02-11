from recrutamento.models import Instituicao

from .base_viewset_test import BaseViewsetTest


class TestInstituicaoViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de Instituicao.
    """

    app = "recrutamento"
    model = Instituicao
    valid_payload = {
        "nome": "Área de atuação Teste",
    }
    model_name = "instituicao"
    url_name_list = "instituicoes-list"
    url_name_detail = "instituicoes-detail"
    allowed_methods = ["GET", "HEAD", "OPTIONS"]
