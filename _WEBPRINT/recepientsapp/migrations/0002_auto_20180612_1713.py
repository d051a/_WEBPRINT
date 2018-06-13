# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='envelop',
            options={'verbose_name': 'Конверт', 'verbose_name_plural': 'Конверты', 'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='envelop_format',
            options={'verbose_name': 'Формат конверта', 'verbose_name_plural': 'Форматы конвертов', 'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='recepient',
            options={'verbose_name': 'Получатель', 'verbose_name_plural': 'Получатели', 'ordering': ['-pk']},
        ),
        migrations.RenameField(
            model_name='envelop',
            old_name='title',
            new_name='env_title',
        ),
        migrations.RenameField(
            model_name='envelop_format',
            old_name='title',
            new_name='env_form_title',
        ),
    ]
