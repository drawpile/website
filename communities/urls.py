from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.FrontPage.as_view(), name='frontpage'),
    url(r'^drawpile.net/ccg/$', views.GuideLinesPage.as_view(), name='ccg'),
    url(r'^drawpile.net/ych/$', views.YchPage.as_view(), name='ych'),
    url(r'^drawpile.net/submit/$', views.SubmitPage.as_view(), name='submit'),
    url(r'^(?P<slug>[-\w]+)/$', views.CommunityPage.as_view(), name='community'),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.EditPage.as_view(), name='edit'),
    url(r'^(?P<slug>[-\w]+)/members/$', views.Memberlist.as_view(), name='memberlist'),
    url(r'^(?P<slug>[-\w]+)/review/$', views.review_community, name='review'),
    url(r'^(?P<slug>[-\w]+)/i-am-old-enough/$', views.community_confirm_age, name='confirm-age'),
    url(r'^(?P<slug>[-\w]+)/server-help/$', views.ServerHelpPage.as_view(), name='server-help'),
]

