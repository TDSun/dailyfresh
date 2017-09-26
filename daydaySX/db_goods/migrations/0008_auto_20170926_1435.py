# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_goods', '0007_auto_20170926_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_url',
            field=models.CharField(verbose_name='图片', max_length=100),
        ),
    ]
