from rest_framework import serializers

from commands.models import Command, Message, Bot, APIKey, RoomID, GeneralSettings


class APICommandSerializer(serializers.ModelSerializer):
    messages = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Command
        fields = ('name', 'messages')


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("text", "command",)
        model = Message


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
