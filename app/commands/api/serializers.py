from rest_framework import serializers

from commands.models import Command, Message, Bot, APIKey, RoomID, GeneralSettings, Timeline


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("text", "command",)
        model = Message


class APICommandSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = Command
        fields = '__all__'


class BotSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Bot


class APIKeySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = APIKey


class RoomIDSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = RoomID


class GeneralSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = GeneralSettings


class TimelineSerializer(serializers.ModelSerializer):
    commands = APICommandSerializer(many=True)
    class Meta:
        fields = '__all__'
        model = Timeline
