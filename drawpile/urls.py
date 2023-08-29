from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView
from django.conf import settings

from templatepages.views import TemplatePageView

urlpatterns = [
    path('_admin/', admin.site.urls),
    path('api/', include('drawpile.api_urls')),
    path('news/', include('news.urls')),
    path('accounts/', include('dpusers.urls')),
    path('communities/', include('communities.urls')),
    path('invites/', include('invites.urls')),
    path('readonly/', TemplateView.as_view(template_name='readonly.html')
        if settings.DRAWPILE_READONLY_SITE
        else RedirectView.as_view(url='/', permanent=False)),
    path('', TemplateView.as_view(template_name='pages/index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

urlpatterns += [
    re_path(r'^(?P<path>.*)/$', TemplatePageView.as_view()),
]
