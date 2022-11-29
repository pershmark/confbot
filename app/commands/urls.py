from django.urls import path
from django.views.static import serve
from django.conf.urls.static import static

from app import settings

app_name = "commands"


urlpatterns = [
    # path('commands/<str:id>', commands, name='commands'),
]