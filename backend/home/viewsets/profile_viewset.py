from novadata_utils.viewsets import NovadataModelViewSet

from home.models import Profile
from home.serializers import ProfileSerializer


class ProfileViewSet(NovadataModelViewSet):
    queryset = Profile.objects.all()

    serializer_class = ProfileSerializer

    search_fields = []
