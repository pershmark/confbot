from rest_framework import generics, status, mixins
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from commands.api.serializers import APICommandSerializer, GeneralSettingsSerializer, RoomIDSerializer, \
    APIKeySerializer, BotSerializer
from commands.models import Command, Bot, APIKey, RoomID, GeneralSettings


class CommandView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Command.objects.all()
    serializer_class = APICommandSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BotView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class APIKeyView(ListAPIView):
    queryset = APIKey.objects.filter(active=True)
    serializer_class = APIKeySerializer


class RoomIDView(ListAPIView):
    queryset = RoomID.objects.filter(active=True)
    serializer_class = RoomIDSerializer


class GeneralSettingsView(ListAPIView):
    queryset = GeneralSettings.objects.filter(active=True)
    serializer_class = GeneralSettingsSerializer
