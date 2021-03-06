# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-10 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0036_auto_20191210_1151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sentenvelop',
            options={'ordering': ['-pk'], 'verbose_name': 'Отправленое', 'verbose_name_plural': 'Отправленные'},
        ),
        migrations.AlterField(
            model_name='sentenvelop',
            name='registry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recepientsapp.Registry'),
        ),
    ]
