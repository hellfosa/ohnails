# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170412_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='uploaded_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]