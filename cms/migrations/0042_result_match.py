# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0041_remove_match_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='match',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cms.Match'),
            preserve_default=False,
        ),
    ]
