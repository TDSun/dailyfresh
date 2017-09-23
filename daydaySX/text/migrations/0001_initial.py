# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('updata_time', models.DateField(verbose_name='更新时间', auto_now=True)),
                ('username', models.CharField(verbose_name='用户名', max_length=20)),
                ('password', models.CharField(verbose_name='密码', max_length=40)),
                ('email', models.CharField(verbose_name='邮箱', max_length=20)),
            ],
            options={
                'db_table': 's_user_account',
            },
        ),
    ]
