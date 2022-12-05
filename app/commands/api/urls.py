from django.urls import path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from app import settings
from commands.api.views import CommandView, BotView, APIKeyView, RoomIDView, GeneralSettingsView

admin.autodiscover()

app_name = 'command_api'

urlpatterns = [
    path('command', CommandView.as_view(), name='get_command'),
    path('bots', BotView.as_view(), name='get_bots'),
    path('api_key', APIKeyView.as_view(), name='api_key'),
    path('general_settings', GeneralSettingsView.as_view(), name='general_settings'),
    path('room_id', RoomIDView.as_view(), name='room_id'),
]
