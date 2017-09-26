# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateField(verbose_name='创建时间', auto_now_add=True)),
                ('updata_time', models.DateField(verbose_name='更新时间', auto_now=True)),
                ('goods_type_id', models.SmallIntegerField(verbose_name='商品类型', choices=[(1, '新鲜水果'), (2, '海鲜水产'), (3, '猪牛羊肉'), (4, '禽类蛋品'), (5, '新鲜蔬菜'), (6, '速冻食品')], default=1)),
                ('goods_name', models.CharField(verbose_name='商品名称', max_length=20)),
                ('goods_sub_title', models.CharField(verbose_name='商品副标题', max_length=128)),
                ('goods_price', models.DecimalField(verbose_name='商品价格', max_digits=10, decimal_places=2)),
                ('transit_price', models.DecimalField(verbose_name='商品运费', max_digits=10, decimal_places=2)),
                ('goods_unite', models.CharField(verbose_name='商品单位', max_length=10)),
                ('goods_info', tinymce.models.HTMLField(verbose_name='商品描述')),
                ('goods_image', models.ImageField(verbose_name='商品图片', upload_to='goods')),
                ('goods_stock', models.IntegerField(verbose_name='商品库存', default=0)),
                ('goods_sales', models.IntegerField(verbose_name='商品销量', default=0)),
                ('goods_status', models.SmallIntegerField(verbose_name='商品状态', choices=[(0, '下线商品'), (1, '上线商品')], default=1)),
            ],
            options={
                'db_table': 's_goods',
            },
        ),
    ]
