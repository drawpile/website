from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.NewsListView.as_view(), name="list"),
    path('feed.atom', views.NewsFeed(), name="atom-feed"),
    path('release-2.3.0-beta.1/', RedirectView.as_view(url="/news/release-2.3.0-beta.2/", permanent=True)),
    path('<slug>/', views.NewsDetailView.as_view(), name='detail'),
]

