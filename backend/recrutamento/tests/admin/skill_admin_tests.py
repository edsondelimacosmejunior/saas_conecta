from recrutamento.admin.skill_admin import SkillAdmin
from recrutamento.models import Skill

from .base_admin_test import BaseAdminTest


class SkillAdminTest(BaseAdminTest):
    admin_class = SkillAdmin
    app = "recrutamento"
    model = Skill
    model_name = "skill"

    def setUp(self):
        super().setUp()

        self.valid_payload = {
            "nome": "Skill Teste",
            "tipo": "HARD",
            "descricao": "Descrição da skill teste",
        }
