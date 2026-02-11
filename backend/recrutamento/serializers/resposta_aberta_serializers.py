from rest_framework import serializers

from ..models import RespostaAberta


class RespostaAbertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostaAberta
        fields = '__all__'
