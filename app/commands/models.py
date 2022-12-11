import datetime

from django.db import models


class BaseModel(models.Model):
    """
    Base abstract model for all models
    """
    class Meta:
        abstract = True
    create_date = models.DateField(null=True, default=datetime.date.today, editable=True)
    write_date = models.DateField(null=True, auto_now=True, editable=True)


class Timeline(BaseModel):
    """
    Timeline
    """
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-create_date"]
        verbose_name = "Timeline"
        verbose_name_plural = "Timelines"


class Command(BaseModel):
    """
    Command
    """
    name = models.TextField(max_length=64, null=False, blank=False, unique=True)
    time = models.TimeField(null=True, blank=True, unique=True)
    timeline = models.ForeignKey(to=Timeline, related_name='commands', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        desc = str([command.text for command in self.messages.all()]).replace('[', '').replace(']', '')
        desc = desc[:200] + '...' if len(desc) > 199 else desc
        return f'Command {self.name}: {desc}...'

    class Meta:
        ordering = ["-create_date"]
        verbose_name = "Command"
        verbose_name_plural = "Commands"


class Message(BaseModel):
    """
    Command
    """
    text = models.TextField(max_length=1024, null=False, blank=False)
    command = models.ForeignKey(to=Command, related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-create_date"]
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class Bot(BaseModel):
    """
    Bot
    """
    first_name = models.CharField(max_length=128, null=False, blank=False)
    last_name = models.CharField(max_length=128, null=False, blank=False)
    username = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    geo = models.CharField(max_length=2, null=False, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ["-create_date"]


class APIKey(BaseModel):
    """
    API Key for Clickmeeting
    """
    key = models.CharField(max_length=512, null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return self.key


class RoomID(BaseModel):
    """
    Room ID for Clickmeeting conf
    """
    room_id = models.CharField(max_length=512, null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return self.room_id


class GeneralSettings(BaseModel):
    """
    max_amount_of_bots - Max amount of bots
    number_of_messages_min - Minimum number of messages that will be sent by bots
    number_of_messages_max - Maximum number of messages that will be sent by bots
    delay_between_messages_min - Delay between messages minimum
    delay_between_messages_max - Delay between messages maximum
    """
    max_amount_of_bots = models.SmallIntegerField(null=False, blank=False)
    number_of_messages_min = models.SmallIntegerField(null=False, blank=False)
    number_of_messages_max = models.SmallIntegerField(null=False, blank=False)
    delay_between_messages_min = models.SmallIntegerField(null=False, blank=False)
    delay_between_messages_max = models.SmallIntegerField(null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)
    geo = models.CharField(max_length=2, null=False, blank=False)
    timeline = models.ForeignKey(to=Timeline, related_name='general_settings', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'GeneralSettings' + '_' + str(self.pk)

    class Meta:
        ordering = ["-create_date"]
