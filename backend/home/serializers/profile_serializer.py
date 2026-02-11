from novadata_utils.serializers import NovadataModelSerializer

from home.models import Profile


class ProfileSerializer(NovadataModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
