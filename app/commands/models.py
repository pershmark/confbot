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


class Command(BaseModel):
    """
    Command
    """
    name = models.TextField(max_length=64, null=False, blank=False, unique=True)

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

