# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_auto_20170208_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='handle',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='match_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
