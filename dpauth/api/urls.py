from django.conf.urls import include, url
from rest_framework import routers

from .viewsets import UsernameViewSet

router = routers.DefaultRouter()

router.register(r'', UsernameViewSet, basename='username')

urlpatterns = [
    url(r'^', include(router.urls)),
    ]
