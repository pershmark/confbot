from rest_framework import serializers

from commands.models import Command, Message


class APICommandSerializer(serializers.ModelSerializer):
    messages = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Command
        fields = ('name', 'messages')


class APICommandSerializerResponse(serializers.ModelSerializer):

    class Meta:
        model = Command
        fields = ('name',)


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("text", "command",)
        model = Message
