from rest_framework import serializers
from Api.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
                  'id',
                  'username',
                  'password',
                  'deposit',
                  'name')
