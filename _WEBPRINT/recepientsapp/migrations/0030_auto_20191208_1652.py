# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-08 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0029_auto_20191207_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistryTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название шаблона')),
                ('template', models.FileField(upload_to='', verbose_name='Шаблон реестра')),
            ],
            options={
                'verbose_name': 'Шаблон реестра',
                'verbose_name_plural': 'Шаблоны реестра',
                'ordering': ['-pk'],
            },
        ),
        migrations.DeleteModel(
            name='RegistryType',
        ),
    ]
