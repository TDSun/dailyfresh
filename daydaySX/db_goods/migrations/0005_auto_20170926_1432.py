# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_goods', '0004_auto_20170926_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='goods',
            new_name='goods_id',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='url',
            new_name='image_url',
        ),
    ]
