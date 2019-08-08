from django.db import models
from apps.login.models import User

class Products(models.Model):
    title = models.CharField(max_length=140)
    colorway = models.CharField(max_length=140)
    size = models.IntegerField(max_length=2)
    id = models.CharField(ma_length=240)


class Order(models.Model):
    order_number = models.IntegerField()
    amount = models.IntegerField()
    user = models.ForeignKey()