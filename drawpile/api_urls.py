from django.conf.urls import url, include

urlpatterns = [
    url(r'^ext-auth/', include('dpauth.urls')),
    ]

