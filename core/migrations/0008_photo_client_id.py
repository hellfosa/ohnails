# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_photo_client_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='client_id',
            field=models.IntegerField(default=0),
        ),
    ]