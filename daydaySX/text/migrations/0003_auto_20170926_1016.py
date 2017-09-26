# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0002_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='updata_time',
            new_name='update_time',
        ),
        migrations.RenameField(
            model_name='passport',
            old_name='updata_time',
            new_name='update_time',
        ),
    ]
