from django.conf.urls import url

from .views import ExtAuthView

urlpatterns = [
    url(r'^$', ExtAuthView.as_view(), name='ext-auth-view'),
    ]

