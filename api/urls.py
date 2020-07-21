from django.urls import include, path
from rest_framework import routers
from .views import AgentViewSet, EventViewSet

router = routers.DefaultRouter()

router.register(r'events', EventViewSet)
router.register(r'agents', AgentViewSet)
