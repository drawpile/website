from django.conf.urls import include, url
from rest_framework import routers

from .viewsets import CommunityViewSet

router = routers.DefaultRouter()

router.register(r'', CommunityViewSet, basename='community')

urlpatterns = [
    url(r'^', include(router.urls)),
    ]
