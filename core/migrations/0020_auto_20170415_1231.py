# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_work_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='work_category',
            new_name='work_categorie',
        ),
    ]