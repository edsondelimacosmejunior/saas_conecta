from django.core.files.uploadedfile import SimpleUploadedFile
from model_bakery import baker

from recrutamento.admin.candidato_admin import CandidatoAdmin
from recrutamento.models import Candidato

from .base_admin_test import BaseAdminTest


class CandidatoAdminTest(BaseAdminTest):
    admin_class = CandidatoAdmin
    app = "recrutamento"
    model = Candidato
    model_name = "candidato"

    def setUp(self):
        super().setUp()

        file = SimpleUploadedFile("file.txt", b"0" * 1024 * 100)
        self.vaga = baker.make("recrutamento.Vaga")

        self.valid_payload = {
            "nome": "Candidato Teste",
            "vaga": self.vaga.id,
            "data_nascimento": "2000-01-01",
            "sobre_mim": "Descrição da candidato teste",
            "estado": "RN",
            "email": "candidato@novadata.com.br",
            "whatsapp": "84999999999",
            "expectativa_2anos": "O céu é o limite",
            "expectativa_10anos": "O universo é o limite",
            "comunicativo": True,
            "ingles": 3,
            "empregado": True,
            "disponibilidade": "IMEDIATA",
            "horarios": "FULL-TIME",
            "pretensao_salarial_pj": 1000.00,
            "pretensao_salarial_clt": 2000.00,
            "curriculo": file,
            "github_portfolio": "https://www.google.com",
            "linkedin": "https://www.google.com",
            "respostaaberta_set-TOTAL_FORMS": "0",  # Nenhum formulário enviado
            "respostaaberta_set-INITIAL_FORMS": "0",  # Nenhum formulário existente
            "respostaaberta_set-MIN_NUM_FORMS": "0",  # Número mínimo de formulários
            "respostaaberta_set-MAX_NUM_FORMS": "1000",
            "skillcandidato_set-TOTAL_FORMS": "0",  # Nenhum formulário enviado
            "skillcandidato_set-INITIAL_FORMS": "0",  # Nenhum formulário existente
            "skillcandidato_set-MIN_NUM_FORMS": "0",  # Número mínimo de formulários
            "skillcandidato_set-MAX_NUM_FORMS": "1000",
            "formacaocandidato_set-TOTAL_FORMS": "0",  # Nenhum formulário enviado
            "formacaocandidato_set-INITIAL_FORMS": "0",  # Nenhum formulário existente
            "formacaocandidato_set-MIN_NUM_FORMS": "0",  # Número mínimo de formulários
            "formacaocandidato_set-MAX_NUM_FORMS": "1000",
        }
