from django.db import models
from db.base_model import BaseModle
# Create your models here.
from utlis.get_has import hex_has


class PassportManager(models.Manager):

    def add_one_passport(self,username,password,email):
        password = hex_has(password)
        passport = self.model(username=username,password=password,email=email)
        passport.save()
        return passport

    def verify_username(self,name):
        try:
            Passport.objects.get(username=name)
            return 'no'
        except Exception:
            return 'yes'



class Passport(BaseModle):
    username = models.CharField(max_length=20,null=False,verbose_name='用户名')
    password = models.CharField(max_length=40,null=False,verbose_name='密码')
    email = models.CharField(max_length=20,null=False,verbose_name='邮箱')

    objects = PassportManager()

    class Meta:
        db_table = 's_user_account'