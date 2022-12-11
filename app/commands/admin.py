from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AdminTimeWidget
from django.forms import Textarea
import nested_admin
from nested_admin.nested import NestedTabularInline

from commands.models import Command, Message, models, Bot, APIKey, RoomID, GeneralSettings, Timeline


# Register your models here.


class MessageAdmin(NestedTabularInline):
    model = Message
    fields = 'text',
    show_change_link = True
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 170})},
    }


class CommandInLineAdmin(NestedTabularInline):
    model = Command
    fields = 'name', 'time',
    show_change_link = True
    extra = 0
    inlines = [MessageAdmin]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 170})},
    }

    class Media:
        js = ('js/clock_time_selections.js',)

class TimelineAdmin(nested_admin.NestedModelAdmin):
    model = Timeline
    fields = 'name',
    show_change_link = True
    save_as = True
    extra = 0
    inlines = [CommandInLineAdmin]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 170})},
    }


class CommandAdmin(nested_admin.NestedModelAdmin):
    model = Command
    fields = 'name',
    show_change_link = True
    save_as = True
    extra = 0
    inlines = [MessageAdmin,]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 170})},
    }


class BotAdmin(admin.ModelAdmin):
    exclude = ('create_date',)
    list_display = ('first_name', 'last_name', 'email', 'username', 'geo')
    list_filter = ('geo',)


class APIKeyAdmin(admin.ModelAdmin):
    exclude = ('create_date',)
    list_display = 'key', 'active',
    list_editable = 'active',

class RoomIDAdmin(admin.ModelAdmin):
    exclude = ('create_date',)
    list_display = 'room_id', 'active',
    list_editable = 'active',


class GeneralSettingsAdmin(admin.ModelAdmin):
    exclude = ('create_date',)
    fields = (
        'active',
        'geo',
        'max_amount_of_bots',
        ('number_of_messages_min', 'number_of_messages_max'),
        ('delay_between_messages_min', 'delay_between_messages_max')
    )
    list_display = ('max_amount_of_bots', 'number_of_messages_min', 'number_of_messages_max',
                    'delay_between_messages_min', 'delay_between_messages_max', 'geo', 'active',)

    list_editable = 'active',


admin.site.register(Command, CommandAdmin)
admin.site.register(Bot, BotAdmin)
admin.site.register(APIKey, APIKeyAdmin)
admin.site.register(RoomID, RoomIDAdmin)
admin.site.register(GeneralSettings, GeneralSettingsAdmin)
admin.site.register(Timeline, TimelineAdmin)
