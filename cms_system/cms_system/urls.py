from django.contrib import admin
from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),

    path('admin/', admin.site.urls),

    path('polls/', include('polls.urls')),
    path('user/', include('user.urls')),
    path('contents/', include('contents.urls')),
    path('display/', include('display.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)