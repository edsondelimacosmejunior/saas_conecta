from recrutamento.models import Skill

from .base_model_test import BaseModelTest


class SkillModelTest(BaseModelTest):
    model = Skill
    required_fields = ["nome"]
    app = "recrutamento"
    model_name = "skill"
    valid_payload = {
        "nome": "Skill",
        "tipo": "HARD",
        "descricao": "Descrição de skill",
    }
