from django.urls import include, path
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path(r'api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path(r'api/', include(router.urls)),
]
