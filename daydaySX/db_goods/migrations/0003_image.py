# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_goods', '0002_auto_20170926_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateField(verbose_name='更新时间', auto_now=True)),
                ('url', models.CharField(verbose_name='图片', max_length=20)),
                ('goods', models.ForeignKey(verbose_name='属于谁', to='db_goods.Goods')),
            ],
            options={
                'db_table': 's_image',
            },
        ),
    ]
