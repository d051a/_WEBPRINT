# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-04 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0012_auto_20191204_0918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sentenvelop',
            options={'ordering': ['pk'], 'verbose_name': 'Отправленое', 'verbose_name_plural': 'Отправленные'},
        ),
        migrations.AddField(
            model_name='sentenvelop',
            name='envelop_format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recepientsapp.Envelop'),
        ),
        migrations.AddField(
            model_name='sentenvelop',
            name='outer_num',
            field=models.CharField(blank=True, max_length=100, verbose_name='Исходящий номер'),
        ),
        migrations.AddField(
            model_name='sentenvelop',
            name='recipient',
            field=models.CharField(blank=True, max_length=150, verbose_name='Получатель'),
        ),
        migrations.AddField(
            model_name='sentenvelop',
            name='rpo_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recepientsapp.RPOType'),
        ),
        migrations.AddField(
            model_name='sentenvelop',
            name='secret_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recepientsapp.SecretType'),
        ),
        migrations.AddField(
            model_name='sentenvelop',
            name='username',
            field=models.CharField(blank=True, max_length=1, verbose_name='Исполнитель'),
        ),
    ]
