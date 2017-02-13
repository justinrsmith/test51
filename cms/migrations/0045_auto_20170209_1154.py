# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0044_auto_20170209_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_half_score', models.IntegerField()),
                ('second_half_score', models.IntegerField()),
                ('overtime_half_score', models.IntegerField()),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Map')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='map',
        ),
        migrations.RemoveField(
            model_name='result',
            name='match',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]