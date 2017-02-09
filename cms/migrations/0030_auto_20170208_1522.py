# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0029_auto_20170208_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='game',
        ),
        migrations.RemoveField(
            model_name='match',
            name='competition',
        ),
        migrations.RemoveField(
            model_name='match',
            name='results',
        ),
        migrations.RemoveField(
            model_name='match',
            name='team',
        ),
        migrations.RemoveField(
            model_name='result',
            name='map',
        ),
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='cms.Player'),
        ),
        migrations.DeleteModel(
            name='Map',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
