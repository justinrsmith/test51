# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20170207_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='order',
        ),
        migrations.AlterField(
            model_name='page',
            name='is_home_page',
            field=models.BooleanField(),
        ),
    ]