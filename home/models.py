from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    gender= models.CharField(max_length=10)
    phone = models.BigIntegerField()
    dob = models.CharField(max_length=70)
    house = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    
class Seller (models. Model):
    name = models.CharField (max_length=40) 
    username = models. CharField(max_length=60)
    email  = models. CharField (max_length=40) 
    password = models. CharField(max_length=30) 
    account = models.BigIntegerField()
    phone = models.BigIntegerField()
    ifsc = models. BigIntegerField()
    address = models.CharField(max_length=200) 
    sellerpic = models. ImageField(upload_to='seller/')    
    status = models.CharField(max_length=20,default='pending')
