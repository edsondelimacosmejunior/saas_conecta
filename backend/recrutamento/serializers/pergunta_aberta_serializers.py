from rest_framework import serializers

from ..models import PerguntaAberta


class PerguntaAbertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerguntaAberta
        fields = '__all__'
