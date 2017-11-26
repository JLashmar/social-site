# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0007_auto_20171123_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='channel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]