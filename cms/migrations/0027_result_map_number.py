# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0026_remove_match_match_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='map_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
