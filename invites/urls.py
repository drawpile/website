from django.urls import re_path

from . import views

app_name = 'invites'
urlpatterns = [
    re_path(r'^(?P<host>[^/:]{1,255}|\[[0-9a-fA-F\:\.]{1,64}\])(?P<port>:[0-9]{1,5}|)/+(?P<session>[a-zA-Z0-9:-]{1,50})/*$', views.InviteView.as_view(), name="invite"),
]

