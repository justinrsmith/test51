# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0037_auto_20170209_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='result',
        ),
        migrations.AddField(
            model_name='match',
            name='result',
            field=models.ManyToManyField(to='cms.Result'),
        ),
    ]
