from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^ko/polls/', include('polls.urls')), # CMS 메인페이지가 203.250.33.53/ko/
    re_path(r'^ko/contents/', include('contents.urls')), # CMS 메인페이지가 203.250.33.53/ko/
    re_path(r'^ko/customUser/', include('customUser.urls')), # CMS 메인페이지가 203.250.33.53/ko/
    re_path(r'^ko/display/', include('display.urls')), # CMS 메인페이지가 203.250.33.53/ko/

]


urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
