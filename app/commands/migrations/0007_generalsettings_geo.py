# Generated by Django 4.1.3 on 2022-12-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0006_apikey_active_generalsettings_active_roomid_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsettings',
            name='geo',
            field=models.CharField(default='en', max_length=2),
            preserve_default=False,
        ),
    ]
