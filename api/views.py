from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated


from .filters import CustomSearchFilter
from .models import Event, Agent
from .serializers import EventSerializer, AgentSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = [u'get', u'post', u'put', u'delete']
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, CustomSearchFilter]
    search_fields = ['description', 'agent__address']
    filter_fields = ['agent__env', 'level']
    ordering_fields = ['level']


class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agents to be viewed or edited.
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    http_method_names = [u'get', u'post', u'put', u'delete']
    permission_classes = [IsAuthenticated]
