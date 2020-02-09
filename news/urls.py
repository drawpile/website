from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.NewsListView.as_view(), name="list"),
    path('feed.atom', views.NewsFeed(), name="atom-feed"),
    path('<slug>/', views.NewsDetailView.as_view(), name='detail'),
]

