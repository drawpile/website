from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.NewsListView.as_view(), name="list"),
    url(r'^(?P<slug>[-.\w]+)/$', views.NewsDetailView.as_view(), name='detail'),
]

