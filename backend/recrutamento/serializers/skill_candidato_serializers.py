from rest_framework import serializers

from ..models import SkillCandidato


class SkillCandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCandidato
        fields = '__all__'
