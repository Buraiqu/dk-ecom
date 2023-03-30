from django.db import models
from home.models import *
from seller.models import *
# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)   
    product = models.ForeignKey(Products,on_delete=models.CASCADE)   
    variant = models.ForeignKey(Variant,on_delete=models.CASCADE)
    qty = models.IntegerField()