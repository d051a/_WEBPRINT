# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-04 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0010_auto_20191204_0914'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RPO',
            new_name='RPOType',
        ),
    ]
