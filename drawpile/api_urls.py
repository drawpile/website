from django.conf.urls import url, include

urlpatterns = [
    url(r'^ext-auth/', include('dpauth.urls')),
    url(r'^gallery/', include('gallery.api_urls')),
    ]

