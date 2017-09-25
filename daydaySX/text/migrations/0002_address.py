# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('updata_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('recipicent_name', models.CharField(max_length=20, verbose_name='收件人')),
                ('recipicent_addr', models.CharField(max_length=256, verbose_name='收件地址')),
                ('zip_code', models.CharField(max_length=6, verbose_name='邮编')),
                ('recipicent_phone', models.CharField(max_length=11, verbose_name='电话')),
                ('is_default', models.BooleanField(default=False, verbose_name='默认地址')),
                ('passport', models.ForeignKey(to='text.Passport', verbose_name='外键')),
            ],
            options={
                'db_table': 's_user_address',
            },
        ),
    ]
