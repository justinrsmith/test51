# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20170204_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='cms.Tag'),
        ),
    ]
