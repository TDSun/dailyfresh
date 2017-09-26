from django.db import models

class Basemanager(models.Manager):

    def save_one_model(self,**kwargs):
        obj = self.model(**kwargs)
        obj.save()
        return obj

    def get_one_moder(self,**kwargs):
        try:
            obj = self.get(**kwargs)
        except Exception:
            obj = None
        return obj

    def get_filter_moder(self,goods_type_id={},order_by=()):
        try:
            obj = self.filter(**goods_type_id).order_by(*order_by)
        except Exception:
            obj = None
        return obj