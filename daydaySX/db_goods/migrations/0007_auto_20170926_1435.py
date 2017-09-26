# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_goods', '0006_auto_20170926_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_url',
            new_name='img_url',
        ),
    ]
