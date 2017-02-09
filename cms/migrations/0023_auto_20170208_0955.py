# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20170208_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='result',
        ),
        migrations.AddField(
            model_name='match',
            name='map',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cms.Map'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='opposing_score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='team_score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='match_type',
            field=models.CharField(choices=[('BO1', 'Best of 1'), ('BO3', 'Best of 3'), ('BO5', 'Best of 5'), ('BO7', 'Best of 7')], default='BO1', max_length=3),
        ),
    ]