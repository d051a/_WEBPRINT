# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0002_auto_20180612_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.AlterModelOptions(
            name='recepient',
            options={'verbose_name': 'Получатель', 'verbose_name_plural': 'Получатели', 'ordering': ['title']},
        ),
    ]
