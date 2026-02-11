from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Beneficio
from ..serializers import BeneficioSerializer


class BeneficioViewSet(NovadataModelViewSet):
    queryset = Beneficio.objects.all()
    serializer_class = BeneficioSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "head", "options"]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    search_fields = ["nome"]

    filterset_fields = [
        "usuario_criacao",
        "usuario_atualizacao",
    ]
