# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 01:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0002_contestentry_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestentry',
            name='datetime_submitted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
