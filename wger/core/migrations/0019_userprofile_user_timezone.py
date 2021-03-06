# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-29 15:32
from __future__ import unicode_literals

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20180829_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_timezone',
            field=timezone_field.fields.TimeZoneField(default='UTC', help_text='Enter exact timzone for your location', verbose_name='Set Timezone'),
        ),
    ]
