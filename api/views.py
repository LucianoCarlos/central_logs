from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Event, Agent, User, Group
from .serializers import EventSerializer, AgentSerializer, UserSerializer, GroupSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
