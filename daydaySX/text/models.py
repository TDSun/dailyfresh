from django.db import models
from db.base_model import BaseModle
from db.base_manager import Basemanager
# Create your models here.
from utlis.get_has import hex_has


class PassportManager(Basemanager):

    def verify(self,name,password=None):
        try:
            if password:
              obj = self.get(username=name,password=hex_has(password))
            else:
              obj = self.get(username=name)
        except Exception:
            obj = None
        return obj


class Passport(BaseModle):
    username = models.CharField(max_length=20,null=False,verbose_name='用户名')
    password = models.CharField(max_length=40,null=False,verbose_name='密码')
    email = models.CharField(max_length=20,null=False,verbose_name='邮箱')

    objects = PassportManager()

    class Meta:
        db_table = 's_user_account'


class Addressmanager(Basemanager):
    pass

class Address(BaseModle):
    recipicent_name = models.CharField(max_length=20,verbose_name='收件人')
    recipicent_addr = models.CharField(max_length=256,verbose_name='收件地址')
    zip_code = models.CharField(max_length=6,verbose_name='邮编')
    recipicent_phone = models.CharField(max_length=11,verbose_name='电话')
    is_default = models.BooleanField(default=False,verbose_name='默认地址')
    passport = models.ForeignKey('Passport',verbose_name='外键')

    objects = Addressmanager()

    class Meta:
        db_table = 's_user_address'