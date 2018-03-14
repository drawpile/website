from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.FrontPage.as_view(), name='frontpage'),
    url(r'^view/(?P<pk>\d+)/$', views.ViewSubmission.as_view(), name='view-submission'),
    url(r'^view/(?P<pk>\d+)/comment/$', views.CommentSubmission.as_view(), name='comment-submission'),
    url(r'^view/(?P<submission_pk>\d+)/comment/(?P<pk>\d+)$', views.EditComment.as_view(), name='edit-comment'),
    url(r'^view/(?P<pk>\d+)/favorite/$', views.ChangeFavoriteComment.as_view(), name='change-submission-favorite'),
    url(r'^user/(?P<pk>\d+)/$', views.UserPage.as_view(), name='userpage'),
    url(r'^groups/$', views.GroupList.as_view(), name='group-list'),
    url(r'^groups/new/$', views.CreateGroup.as_view(), name='group-new'),
    url(r'^group/(?P<slug>[-\w]+)/$', views.GroupDetail.as_view(), name='group-detail'),
    url(r'^group/(?P<slug>[-\w]+)/edit/$', views.EditGroup.as_view(), name='group-edit'),
    url(r'^group/(?P<slug>[-\w]+)/leave/$', views.LeaveGroup.as_view(), name='group-leave'),
    url(r'^group/(?P<slug>[-\w]+)/pending/$', views.GroupPending.as_view(), name='group-pending'),
    url(r'^submit/$', views.SubmitView.as_view(), name='submit'),
    url(r'^edit/(?P<pk>\d+)/$', views.EditSubmission.as_view(), name='edit-submission'),
]

