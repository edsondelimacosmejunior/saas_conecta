from rest_framework import serializers

from ..models import Vaga


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = [
            "id",
            "titulo",
            "sobre",
            "slug",
            "ativa",
            "responsabilidades",
            "data_fechamento",
            "salario",
            "tipo_contratacao",
            "vaga_generica",
            "tipo_regime_trabalho",
            "area_atuacao",
            "data_criacao",
            "data_atualizacao",
            "usuario_criacao",
            "usuario_atualizacao",
        ]
