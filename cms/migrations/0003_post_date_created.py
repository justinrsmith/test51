# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 17:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_game_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 4, 17, 12, 34, 540611, tzinfo=utc)),
        ),
    ]
