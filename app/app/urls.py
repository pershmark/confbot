from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve

from app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('commands.urls')),
    path('api/', include('commands.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
                ]

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



admin.site.site_header = 'Commands Manager'
admin.site.site_title = 'Commands Manager'
