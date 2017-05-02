from django.contrib.auth.models import User, Group
# import all api models
from api.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = trips
        fields = ('tripid', 'tripdate', 'provider', 'status', 'pickzip', 'dropzip', 'shared')
