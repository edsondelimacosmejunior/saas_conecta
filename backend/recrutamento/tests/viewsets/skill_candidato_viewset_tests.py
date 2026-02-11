from model_bakery import baker

from recrutamento.models import SkillCandidato

from .base_viewset_test import BaseViewsetTest


class TestSkillCandidatoViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de SkillCandidato.
    """

    app = "recrutamento"
    model = SkillCandidato
    model_name = "skill_candidato"
    url_name_list = "skills-candidatos-list"
    url_name_detail = "skills-candidatos-detail"
    allowed_methods = ["GET", "POST", "HEAD", "OPTIONS"]

    def setUp(self):
        self.candidato = baker.make("recrutamento.Candidato")
        self.skill = baker.make("recrutamento.Skill")

        self.valid_payload = {
            "candidato": self.candidato.id,
            "skill": self.skill.id,
            "avaliacao": 3,
            "tempo_experiencia": 4,
        }

        super().setUp()
