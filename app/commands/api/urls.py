from django.urls import path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from app import settings
from commands.api.views import CommandView


admin.autodiscover()

app_name = 'command_api'

urlpatterns = [
    path('command', CommandView.as_view(), name='get_command'),
]
