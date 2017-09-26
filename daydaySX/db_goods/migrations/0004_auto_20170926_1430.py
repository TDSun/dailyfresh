# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_goods', '0003_image'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='image',
            table='s_goods_image',
        ),
    ]
