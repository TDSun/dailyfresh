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