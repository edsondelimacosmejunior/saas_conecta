from rest_framework import serializers

from ..models import FormacaoCandidato


class FormacaoCandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormacaoCandidato
        fields = '__all__'
