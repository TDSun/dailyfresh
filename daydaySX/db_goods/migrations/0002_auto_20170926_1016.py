# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='updata_time',
            new_name='update_time',
        ),
    ]
