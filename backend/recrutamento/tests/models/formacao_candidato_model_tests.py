from model_bakery import baker

from recrutamento.models import FormacaoCandidato

from .base_model_test import BaseModelTest


class FormacaoCandidatoModelTest(BaseModelTest):
    model = FormacaoCandidato
    required_fields = ["nome"]
    app = "recrutamento"
    model_name = "formacao_candidato"

    def setUp(self):
        self.candidato = baker.make("recrutamento.Candidato")
        self.instituicao = baker.make("recrutamento.Instituicao")
        self.curso = baker.make("recrutamento.Curso")

        self.valid_payload = {
            "candidato": self.candidato,
            "instituicao": self.instituicao,
            "curso": self.curso,
            "grau": 5.0,
            "data_inicio": "2020-01-01",
            "data_conclusao": "2020-01-01",
        }

        super().setUp()
