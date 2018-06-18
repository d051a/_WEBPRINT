# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepientsapp', '0003_auto_20180614_1605'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AlterField(
            model_name='envelop',
            name='envelop_template',
            field=models.FileField(verbose_name='Шаблон конверта', upload_to='/home/d051a/Desktop/PythonProjects/webprint/_WEBPRINT/upload/'),
        ),
    ]
