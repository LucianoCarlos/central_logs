# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Event, Agent, User, Group


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
