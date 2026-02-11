from django.core.files.uploadedfile import SimpleUploadedFile
from model_bakery import baker

from recrutamento.models import Candidato

from .base_model_test import BaseModelTest


class CandidatoModelTest(BaseModelTest):
    model = Candidato
    app = "recrutamento"
    model_name = "candidato"

    def setUp(self):
        file = SimpleUploadedFile("file.txt", b"0" * 1024 * 100)
        self.vaga = baker.make("recrutamento.Vaga")

        self.valid_payload = {
            "nome": "Candidato Teste",
            "vaga": self.vaga,
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
        }

        super().setUp()
