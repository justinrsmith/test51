# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 00:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20170204_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='title',
        ),
    ]