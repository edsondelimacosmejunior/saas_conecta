from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Skill
from ..serializers import SkillSerializer


class SkillViewSet(NovadataModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "head", "options"]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    search_fields = ["nome"]

    filterset_fields = [
        "usuario_criacao",
        "usuario_atualizacao",
    ]
