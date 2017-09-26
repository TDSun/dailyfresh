from django.db import models
from db_goods.enums import *
from db.base_manager import Basemanager
from db.base_model import BaseModle
from tinymce.models import HTMLField

class ImageManager(Basemanager):
    pass


class Image(BaseModle):

    goods=models.ForeignKey('Goods',verbose_name='属于谁')
    img_url=models.CharField(max_length=100,verbose_name='图片')

    objects = ImageManager()

    class Meta:
        db_table = 's_goods_image'


class GoodsManager(Basemanager):

    def get_goods_num_byorder(self,num,sort='default',**kwargs):
        order_by = ('-pk',)
        if sort == 'new':
            order_by = ('-create_time',)
        elif sort == 'price':
            order_by = ('goods_price',)
        elif sort == 'hot':
            order_by = ('-goods_sales',)
        obj = self.get_filter_moder(goods_type_id=kwargs,order_by=order_by)
        if num:
            obj = obj[:num]
        return obj

    def get_one_goods_image(self,**kwargs):
        obj = self.get_one_moder(**kwargs)
        image = Image.objects.get_one_moder(goods_id=obj.id)
        obj.images = image.img_url
        print(image.img_url)
        return obj

# Create your models here.
class Goods(BaseModle):
    '''商品模型类'''
    '''
    goods_type_choice = (
        (1, '新鲜水果'),
        (2, '海鲜水产'),
        (3, '猪牛羊肉'),
        (4, '禽类蛋品'),
        (5, '新鲜蔬菜'),
        (6, '速冻食品')
    )
    '''
    goods_type_choice = (
        (FRUIT, GOODS_TYPE[FRUIT]),
        (SEAFOOD, GOODS_TYPE[SEAFOOD]),
        (MEAT, GOODS_TYPE[MEAT]),
        (EGGS, GOODS_TYPE[EGGS]),
        (VEGETABLES, GOODS_TYPE[VEGETABLES]),
        (FROZEN, GOODS_TYPE[FROZEN])
    )
    goods_type_id = models.SmallIntegerField(choices=goods_type_choice, default=FRUIT, verbose_name='商品类型')
    goods_name = models.CharField(max_length=20, verbose_name='商品名称')
    goods_sub_title = models.CharField(max_length=128, verbose_name='商品副标题')
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    transit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品运费')
    goods_unite = models.CharField(max_length=10, verbose_name='商品单位')
    goods_info = HTMLField(verbose_name='商品描述')
    goods_image = models.ImageField(upload_to='goods', verbose_name='商品图片')
    goods_stock = models.IntegerField(default=0, verbose_name='商品库存')
    goods_sales = models.IntegerField(default=0, verbose_name='商品销量')
    # 0:下线商品 1:上线商品
    '''
    goods_status_choice = (
        (0, '下线商品'),
        (1, '上线商品')
    )
    '''
    goods_status_choice = (
        (OFFLINE, GOODS_STATUS[OFFLINE]),
        (ONLINE, GOODS_STATUS[ONLINE])
    )
    goods_status = models.SmallIntegerField(choices=goods_status_choice, default=ONLINE, verbose_name='商品状态')

    objects = GoodsManager() # 如果不需要商品详情图片
    # objects_logic = GoodsLogicManager() # 需要商品详情图片

    class Meta:
        db_table = 's_goods'