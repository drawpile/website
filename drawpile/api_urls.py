from django.conf.urls import url, include
from dpauth.api.extauth_views import ExtAuthView
from dpauth.api.extban_views import ExtBanView

app_name = "api"
urlpatterns = [
    url(r"^ext-auth/$", ExtAuthView.as_view(), name="ext-auth-view"),
    url(r"^ext-bans/(?P<extbankey>.*)/$", ExtBanView.as_view(), name="ext-ban-view"),
    url(r"^users/", include("dpauth.api.urls")),
    url(r"^communities/", include("communities.api.urls")),
]
