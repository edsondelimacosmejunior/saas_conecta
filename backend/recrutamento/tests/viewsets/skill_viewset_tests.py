from recrutamento.models import Skill

from .base_viewset_test import BaseViewsetTest


class TestSkillViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de Skill.
    """

    app = "recrutamento"
    model = Skill
    valid_payload = {
        "nome": "Skill Teste",
    }
    model_name = "skill"
    url_name_list = "skills-list"
    url_name_detail = "skills-detail"
    allowed_methods = ["GET", "HEAD", "OPTIONS"]
