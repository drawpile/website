from django.conf.urls import url, include

from dpauth.api.extauth_views import ExtAuthView

urlpatterns = [
    url(r'^ext-auth/$', ExtAuthView.as_view(), name='ext-auth-view'),
    url(r'^users/', include('dpauth.api.urls')),
]

