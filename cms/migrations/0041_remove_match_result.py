# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 15:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0040_auto_20170209_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='result',
        ),
    ]
