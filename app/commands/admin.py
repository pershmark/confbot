from django.contrib import admin
from django.forms import Textarea

from commands.models import Command, Message, models


# Register your models here.


class MessageAdmin(admin.TabularInline):
    model = Message
    fields = 'text',
    show_change_link = True
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 170})},
    }


class CommandAdmin(admin.ModelAdmin):
    model = Command
    fields = 'name',
    show_change_link = True
    save_as = True
    extra = 0
    inlines = [MessageAdmin,]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 170})},
    }


admin.site.register(Command, CommandAdmin)
