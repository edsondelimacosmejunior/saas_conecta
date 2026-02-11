from recrutamento.models import AreaAtuacao

from .base_viewset_test import BaseViewsetTest


class TestAreaAtuacaoViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de AreaAtuacao.
    """

    app = "recrutamento"
    model = AreaAtuacao
    valid_payload = {
        "nome": "Área de atuação Teste",
    }
    model_name = "area_atuacao"
    url_name_list = "areas-atuacoes-list"
    url_name_detail = "areas-atuacoes-detail"
    allowed_methods = ["GET", "HEAD", "OPTIONS"]
