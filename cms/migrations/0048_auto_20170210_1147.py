# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0047_auto_20170209_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='active',
        ),
        migrations.AddField(
            model_name='team',
            name='is_area_51',
            field=models.BooleanField(default=False),
        ),
    ]