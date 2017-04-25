# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_photo_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='uploaded_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]