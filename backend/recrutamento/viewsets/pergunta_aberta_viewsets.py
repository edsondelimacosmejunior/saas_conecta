from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from ..models import PerguntaAberta
from ..serializers import PerguntaAbertaSerializer


class PerguntaAbertaViewSet(NovadataModelViewSet):
    queryset = PerguntaAberta.objects.all()
    serializer_class = PerguntaAbertaSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "head", "options"]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    search_fields = ["titulo"]

    filterset_fields = [
        "vaga",
        "usuario_criacao",
        "usuario_atualizacao",
    ]
