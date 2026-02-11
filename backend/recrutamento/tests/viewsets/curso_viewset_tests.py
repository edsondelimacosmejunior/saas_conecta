from recrutamento.models import Curso

from .base_viewset_test import BaseViewsetTest


class TestCursoViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de Curso.
    """

    app = "recrutamento"
    model = Curso
    valid_payload = {
        "nome": "Curso Teste",
    }
    model_name = "curso"
    url_name_list = "cursos-list"
    url_name_detail = "cursos-detail"
    allowed_methods = ["GET", "HEAD", "OPTIONS"]
