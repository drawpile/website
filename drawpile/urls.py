from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView
from django.conf import settings

from templatepages.views import DocumentationDetailView, TemplatePageView

urlpatterns = [
    path('_admin/', admin.site.urls),
    path('api/', include('drawpile.api_urls')),
    path('news/', include('news.urls')),
    path('accounts/', include('dpusers.urls')),
    path('auth/', include('dpauth.urls')),
    path('communities/', include('communities.urls')),
    path('invites/', include('invites.urls')),
    path('ban/', RedirectView.as_view(
        url='/communities/drawpile.net/ban/', permanent=True)),
    path('readonly/', TemplateView.as_view(template_name='readonly.html')
        if settings.DRAWPILE_READONLY_SITE
        else RedirectView.as_view(url='/', permanent=False)),
    path('discord/', RedirectView.as_view(url='https://discord.gg/VHRDh2fKnc', permanent=True)),
    path('matrix/', RedirectView.as_view(url='https://matrix.to/#/#drawpile:matrix.org', permanent=True)),
    path('localhosthelp/', RedirectView.as_view(url='https://docs.drawpile.net/help/common/hosting#builtin-server', permanent=True)),
    path('pubrules/', RedirectView.as_view(url='/communities/drawpile.net/ccg/', permanent=True)),
    path('sharedarraybufferhelp/', RedirectView.as_view(url='https://docs.drawpile.net/help/tech/browser#sharedarraybuffer-issues', permanent=True)),
    path('lgm/', TemplateView.as_view(template_name='lgm.html')),
    path('namecheckbot/', TemplateView.as_view(template_name='namecheckbot.html')),
    path('', TemplateView.as_view(template_name='pages/index.html')),
]

if settings.DRAWPILE_IMPRESSUM:
    urlpatterns += path('impressum/', TemplateView.as_view(template_name='impressum.html')),

if settings.DRAWPILE_PRIVACY_POLICY:
    urlpatterns += path('privacy/', TemplateView.as_view(template_name='privacy.html')),

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

urlpatterns += [
    path('docs/<slug:slug>/', DocumentationDetailView.as_view(), name='documentation-detail'),
    re_path(r'^(?P<path>.*)/$', TemplatePageView.as_view()),
]
