# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0006_channel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
