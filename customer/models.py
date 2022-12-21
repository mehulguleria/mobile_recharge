from django.db import models
from datetime import datetime

class recharge_list(models.Model):
    amount = models.IntegerField()
    title = models.CharField(max_length=100,null=False)
    detail = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

class record(models.Model):
    recharge_id = models.IntegerField(default=None)
    phone = models.BigIntegerField(null=False)
    title = models.CharField(max_length=100,null=False,default=None)
    ammount = models.IntegerField()
    detail = models.CharField(max_length=200)
    recharge_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:

        return self.phone

