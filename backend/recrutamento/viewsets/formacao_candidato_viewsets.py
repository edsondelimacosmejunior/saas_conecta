from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from ..models import FormacaoCandidato
from ..serializers import FormacaoCandidatoSerializer


class FormacaoCandidatoViewSet(NovadataModelViewSet):
    queryset = FormacaoCandidato.objects.all()
    serializer_class = FormacaoCandidatoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "head", "options"]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    search_fields = ["candidato__nome"]

    filterset_fields = [
        "candidato",
        "instituicao",
        "curso",
        "usuario_criacao",
        "usuario_atualizacao",
    ]
