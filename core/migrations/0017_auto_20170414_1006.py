# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_work_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='work',
            name='work_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]