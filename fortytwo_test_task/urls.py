
from django.conf.urls import patterns, include, url
from django.contrib import admin
# from fortytwo_test_task import settings
from django.conf import settings
from django.conf.urls.static import static

from apps.hello import urls as hello_urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(hello_urls, namespace='hello')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
