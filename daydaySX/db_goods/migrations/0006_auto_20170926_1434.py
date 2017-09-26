# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_goods', '0005_auto_20170926_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='goods_id',
            new_name='goods',
        ),
    ]
