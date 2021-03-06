# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 02:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0010_auto_20170204_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
