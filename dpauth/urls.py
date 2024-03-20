from django.urls import path, re_path
from . import views

app_name = "auth"
urlpatterns = [
    path("", views.AuthUsernamesView.as_view(), name="usernames"),
    re_path(r"^finish/(?P<name>.+)/$", views.AuthFinishView.as_view(), name="finish"),
    path("login/", views.AuthLoginView.as_view(), name="login"),
    path("logout/", views.AuthLogoutView.as_view(), name="logout"),
    path("ban-analyzer/", views.BanAnalyzerView.as_view(), name="ban-analyzer"),
]
