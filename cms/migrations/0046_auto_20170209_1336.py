# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 19:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0045_auto_20170209_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamresult',
            old_name='overtime_half_score',
            new_name='overtime_score',
        ),
    ]