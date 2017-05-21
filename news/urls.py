from django.conf.urls import url
from django.views.generic import ListView, DetailView

from . import models

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=models.Post.objects.visible(),
        paginate_by=3
    ), name="list"),
    url(r'^(?P<slug>[-.\w]+)/$', DetailView.as_view(
        queryset=models.Post.objects.visible(),
    ), name='detail'),
]

