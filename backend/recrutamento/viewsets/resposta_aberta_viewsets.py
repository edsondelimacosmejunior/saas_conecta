from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from ..models import RespostaAberta
from ..serializers import RespostaAbertaSerializer


class RespostaAbertaViewSet(NovadataModelViewSet):
    queryset = RespostaAberta.objects.all()
    serializer_class = RespostaAbertaSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "head", "options"]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    search_fields = ["candidato__nome"]

    filterset_fields = [
        "pergunta_aberta",
        "candidato",
        "usuario_criacao",
        "usuario_atualizacao",
    ]
