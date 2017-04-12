# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170412_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='photo',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]