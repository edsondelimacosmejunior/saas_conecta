from model_bakery import baker

from recrutamento.models import FormacaoCandidato

from .base_viewset_test import BaseViewsetTest


class TestFormacaoCandidatoViewSet(BaseViewsetTest):
    """
    Classe de teste para o ViewSet de FormacaoCandidato.
    """

    app = "recrutamento"
    model = FormacaoCandidato
    model_name = "formacao_candidato"
    url_name_list = "formacoes-candidatos-list"
    url_name_detail = "formacoes-candidatos-detail"
    allowed_methods = ["GET", "POST", "HEAD", "OPTIONS"]

    def setUp(self):
        self.candidato = baker.make("recrutamento.Candidato")
        self.instituicao = baker.make("recrutamento.Instituicao")
        self.curso = baker.make("recrutamento.Curso")

        self.valid_payload = {
            "candidato": self.candidato.id,
            "instituicao": self.instituicao.id,
            "curso": self.curso.id,
            "grau": 5,
            "data_inicio": "2020-01-01",
            "data_conclusao": "2020-01-01",
        }

        super().setUp()
