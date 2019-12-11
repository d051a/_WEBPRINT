# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-09 14:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0031_auto_20191209_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepient',
            name='adds',
            field=models.CharField(default='address', max_length=100, verbose_name='Адрес, дом, кв.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recepient',
            name='city',
            field=models.CharField(default='Moscow city', max_length=100, verbose_name='Регион(область)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recepient',
            name='region',
            field=models.CharField(default='Moscow region', max_length=100, verbose_name='Регион(область)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recepient',
            name='postcode',
            field=models.CharField(max_length=6, null=True, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Индекс'),
        ),
        migrations.AlterField(
            model_name='recepient',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Наименование адресата'),
        ),
    ]