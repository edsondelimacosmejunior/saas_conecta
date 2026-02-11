from django.contrib.auth.models import User
from novadata_utils.viewsets import NovadataModelViewSet

from home.serializers import UserSerializer


class UserViewSet(NovadataModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer

    search_fields = []
