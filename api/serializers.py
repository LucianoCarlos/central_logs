# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Event, Agent


class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class EventSerializer(serializers.HyperlinkedModelSerializer):
    agent = AgentSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'level', 'title',
                  'description', 'arquivado', 'date', 'agent']
