from django_filters.rest_framework import DjangoFilterBackend
from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ..models import Candidato
from ..serializers import CandidatoCreateSerializer, CandidatoSerializer


class CandidatoViewSet(NovadataModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["post", "head", "options"]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    search_fields = ["nome"]

    filterset_fields = [
        "vaga",
        "usuario_criacao",
        "usuario_atualizacao",
    ]

    def get_serializer(self, *args, **kwargs):
        if self.action == "create":
            return CandidatoCreateSerializer(*args, **kwargs)
        return super(CandidatoViewSet, self).get_serializer(*args, **kwargs)

    def get_data(self, request):
        if request.FILES:
            data = request.data  # Não faz `.copy()` para evitar erro com arquivos
        else:
            data = request.data.copy()  # Mantém `.copy()` apenas quando seguro

        return data


    @action(detail=False, methods=["post"], url_path="verificar-email", permission_classes=[AllowAny])
    def verificar_email(self, request):
        vaga_id = request.data.get("vaga_id")
        email = request.data.get("email")

        if not vaga_id:
            return Response({"detail": "O campo 'vaga_id' é obrigatório."}, status=400)
        if not email:
            return Response({"detail": "O campo 'email' é obrigatório."}, status=400)

        candidato_existe = Candidato.objects.filter(vaga_id=vaga_id, email=email).exists()

        if candidato_existe:
            return Response(
                {"exists": True, "message": "Este e-mail já possui inscrição nesta vaga."},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"exists": False, "message": "Este e-mail ainda não está inscrito nesta vaga."},
                status=status.HTTP_200_OK
            )