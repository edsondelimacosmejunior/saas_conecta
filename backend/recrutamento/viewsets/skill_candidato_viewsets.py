from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from ..models import SkillCandidato
from ..serializers import SkillCandidatoSerializer


class SkillCandidatoViewSet(NovadataModelViewSet):
    queryset = SkillCandidato.objects.all()
    serializer_class = SkillCandidatoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "head", "options"]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    search_fields = [
        "skill__nome",
    ]

    filterset_fields = [
        "candidato",
        "skill",
        "usuario_criacao",
        "usuario_atualizacao",
    ]
