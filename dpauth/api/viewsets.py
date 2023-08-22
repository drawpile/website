from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError

from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .username_serializers import UsernameSerializer

from dpauth.models import Username


class UsernameViewSet(viewsets.ModelViewSet):
    lookup_field = 'name'
    lookup_value_regex = '.+'
    permission_classes = (IsAuthenticated,)
    serializer_class = UsernameSerializer
    parser_classes = (JSONParser, MultiPartParser)

    def get_queryset(self):
        return Username.objects.filter(user=self.request.user)

    def perform_destroy(self, instance):
        if instance.is_primary:
            try:
                secondary = Username.objects.filter(
                    Q(user=self.request.user) &
                    ~Q(id=instance.id))[0]
            except IndexError:
                raise ValidationError("Cannot delete last username")
            secondary.make_primary()
        instance.delete()
