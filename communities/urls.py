from django.urls import path

from . import views


app_name = 'communities'
urlpatterns = [
    path('', views.FrontPage.as_view(), name='frontpage'),
    path('drawpile.net/ccg/', views.GuideLinesPage.as_view(), name='ccg'),
    path('drawpile.net/ych/', views.YchPage.as_view(), name='ych'),
    path('drawpile.net/submit/', views.SubmitPage.as_view(), name='submit'),
    path('<slug>/', views.CommunityPage.as_view(), name='community'),
    path('<slug>/edit/', views.EditPage.as_view(), name='edit'),
    path('<slug>/members/', views.Memberlist.as_view(), name='memberlist'),
    path('<slug>/review/', views.review_community, name='review'),
    path('<slug>/i-am-old-enough/', views.community_confirm_age, name='confirm-age'),
    path('<slug>/server-help/', views.ServerHelpPage.as_view(), name='server-help'),
]

