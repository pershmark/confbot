# Generated by Django 4.1.3 on 2022-12-05 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0005_bot_geo'),
    ]

    operations = [
        migrations.AddField(
            model_name='apikey',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='generalsettings',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='roomid',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]