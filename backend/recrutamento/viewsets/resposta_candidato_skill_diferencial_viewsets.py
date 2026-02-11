from recrutamento.models.resposta_candidato_skill_diferencial import RepostaCandidatoSkillDiferencial
from recrutamento.serializers.resposta_candidato_skill_diferencial_serializers import RepostaCandidatoSkillDiferencialSerializer
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend


class RepostaCandidatoSkillDiferencialViewSet(viewsets.ModelViewSet):
    queryset = RepostaCandidatoSkillDiferencial.objects.all()
    serializer_class = RepostaCandidatoSkillDiferencialSerializer   
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "head", "options"]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    search_fields = [
        'candidato__nome',
        'skill__nome',
    ]
        
    
