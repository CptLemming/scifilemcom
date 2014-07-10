from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.template.response import TemplateResponse

from cms.sitemaps import CMSSitemap

admin.autodiscover()


sitemap_list = {
    'cmspages': CMSSitemap
}


urlpatterns = patterns('',
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': sitemap_list
    }),
    url(r'^robots.txt$',
        lambda request: TemplateResponse(
            request,
            template='robots.txt',
            context={'allow_robots': settings.ALLOW_ROBOTS},
            content_type='text/plain',
        )
    ),
    url(r'^manage/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
