# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('address', models.CharField(verbose_name='Адрес', max_length=100)),
                ('city', models.CharField(verbose_name='Город', max_length=20)),
                ('index', models.CharField(verbose_name='Индекс', max_length=6)),
                ('choices', models.CharField(verbose_name='Тип адреса', max_length=2, default='FT', choices=[('LG', 'Юридический'), ('FT', 'Фактический'), ('PL', 'Почтовый')])),
            ],
        ),
        migrations.CreateModel(
            name='Envelop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название конверта', max_length=30)),
                ('envelop_template', models.FileField(verbose_name='Шаблон конверта', upload_to='/home/d051a/Desktop/PythonProjects/_webprint/_WEBPRINT/upload/')),
            ],
        ),
        migrations.CreateModel(
            name='Envelop_format',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Формат конверта', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Recepient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='ФИО или название организации', max_length=30)),
                ('pub_date', models.DateField(verbose_name='Дата публикации', auto_now_add=True)),
                ('address', models.CharField(verbose_name='Адрес', max_length=100)),
                ('postcode', models.CharField(verbose_name='Индекс', max_length=6, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='envelop',
            name='envelop_format',
            field=models.ForeignKey(to='recepientsapp.Envelop_format'),
        ),
    ]
