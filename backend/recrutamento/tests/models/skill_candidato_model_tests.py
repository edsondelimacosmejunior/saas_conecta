from model_bakery import baker

from recrutamento.models import SkillCandidato

from .base_model_test import BaseModelTest


class SkillCandidatoModelTest(BaseModelTest):
    model = SkillCandidato
    required_fields = ["nome"]
    app = "recrutamento"
    model_name = "skill_candidato"

    def setUp(self):
        self.candidato = baker.make("recrutamento.Candidato")
        self.skill = baker.make("recrutamento.Skill")

        self.valid_payload = {
            "candidato": self.candidato,
            "skill": self.skill,
            "avaliacao": 3,
            "tempo_experiencia": 4,
        }

        super().setUp()
