from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    date_of_add = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'login', 'email', 'name', 'surname',
                  'roles', 'phone', 'date_of_add', 'password')
        extra_kwargs = {'password': {'write_only': True}}