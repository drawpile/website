from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

from templatepages.views import TemplatePageView

urlpatterns = [
    url(r'^_admin/', admin.site.urls),
    url(r'^api/', include('drawpile.api_urls', namespace='api')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^accounts/', include('dpusers.urls', namespace='users')),
    url(r'^$', TemplateView.as_view(template_name='pages/index.html')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^(?P<path>.*)/$', TemplatePageView.as_view()),
]
