from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.FrontPage.as_view(), name='frontpage'),
    url(r'^view/(?P<pk>\d+)/$', views.ViewSubmission.as_view(), name='view-submission'),
    url(r'^user/(?P<pk>\d+)/$', views.UserPage.as_view(), name='userpage'),
    url(r'^groups/$', views.GroupList.as_view(), name='group-list'),
    url(r'^group/(?P<slug>[-\w]+)/$', views.GroupDetail.as_view(), name='group-detail'),
    url(r'^group/(?P<slug>[-\w]+)/leave/$', views.LeaveGroup.as_view(), name='group-leave'),
]

