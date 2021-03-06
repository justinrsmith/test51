# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0048_auto_20170210_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchmapteamresult',
            name='fielded_roster',
        ),
        migrations.AddField(
            model_name='match',
            name='opponent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='opponent', to='cms.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='opponent_roster',
            field=models.ManyToManyField(related_name='opponent_roster', to='cms.TeamPlayer'),
        ),
        migrations.AddField(
            model_name='match',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team', to='cms.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='team_roster',
            field=models.ManyToManyField(related_name='team_roster', to='cms.TeamPlayer'),
        ),
    ]
