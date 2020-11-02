from rest_framework import serializers


# --------------MODELOS-------------------
from Profile.models import ProfileModel
from Profile.models import Users

class ProfileModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields=('__all__')