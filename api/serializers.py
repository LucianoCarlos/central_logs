# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Event, Agent, User, Group


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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    confirm_password = serializers.CharField(
        write_only=True,
        style={'input_type': 'confirm_password'}
    )

    class Meta:
        model = User
        fields = ['url', 'username', 'email',
                  'password', 'confirm_password']

    def create(self, validated_data):
        password = validated_data.get('password')
        confirm_password = validated_data.pop('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})

        user = super(UserSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()

        return User

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        confirm_password = validated_data.pop('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})

        instance.set_password(self.validated_data['password'])
        instance.email = self.validated_data['email']
        instance.username = self.validated_data['username']
        instance.save()
        return instance


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
