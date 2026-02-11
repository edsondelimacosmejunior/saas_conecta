from recrutamento.models import Beneficio

from .base_viewset_test import BaseViewsetTest


class TestBeneficioViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de Beneficio.
    """

    app = "recrutamento"
    model = Beneficio
    valid_payload = {
        "nome": "Beneficio Teste",
    }
    model_name = "beneficio"
    url_name_list = "beneficios-list"
    url_name_detail = "beneficios-detail"
    allowed_methods = ["GET", "HEAD", "OPTIONS"]
