import django_filters.rest_framework
from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Vaga,Candidato
from ..serializers import VagaSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status

class VagaViewSet(NovadataModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "head", "options"]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = [
        "slug",
        "ativa",
        "data_fechamento",
        "tipo_contratacao",
        "tipo_regime_trabalho",
        "area_atuacao",
        "usuario_criacao",
        "usuario_atualizacao",
    ]

    search_fields = ["titulo"]

    @action(methods=["get"], detail=True)
    def beneficios(self, request, pk=None):
        from ..serializers import BeneficioSerializer

        vaga = self.get_object()

        beneficios = vaga.beneficios.all()

        serializer = BeneficioSerializer(beneficios, many=True)

        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    def requisitos(self, request, pk=None):
        from ..serializers import SkillSerializer

        vaga = self.get_object()

        requisitos = vaga.requisitos.all()

        serializer = SkillSerializer(requisitos, many=True)

        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    def diferenciais(self, request, pk=None):
        from ..serializers import SkillSerializer

        vaga = self.get_object()

        diferenciais = vaga.diferenciais.all()

        serializer = SkillSerializer(diferenciais, many=True)

        return Response(serializer.data)

    @action(methods=["get"], detail=True)
    def perguntas_adicionais(self, request, pk=None):
        from ..serializers import PerguntaAbertaSerializer

        vaga = self.get_object()

        perguntas_abertas = vaga.perguntaaberta_set.all()

        serializer = PerguntaAbertaSerializer(perguntas_abertas, many=True)

        return Response(serializer.data)
