from rest_framework import serializers

from ..models import RepostaCandidatoSkillDiferencial


class RepostaCandidatoSkillDiferencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepostaCandidatoSkillDiferencial
        fields = '__all__'
        read_only_fields = [
            'id',
            'data_criacao',
            'data_atualizacao',
            'usuario_criacao',
            'usuario_atualizacao',
        ]