# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0038_auto_20170209_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.ManyToManyField(blank=True, to='cms.Result'),
        ),
    ]
