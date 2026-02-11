from rest_framework import serializers

from ..models import AreaAtuacao


class AreaAtuacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaAtuacao
        fields = '__all__'
