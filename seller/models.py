from django.db import models
from unittest.util import _MAX_LENGTH
from home.models import Seller
from home.models import Customer

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to='products/')
    size_guide = models.ImageField(upload_to='products/',null=True,blank=True)
    material_id = models.ForeignKey("Material", on_delete=models.CASCADE) 
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    fit_id = models.ForeignKey("Fit",on_delete=models.CASCADE,null=True,blank=True) 
    pattern_id = models.ForeignKey("Pattern",on_delete=models.CASCADE,null=True,blank=True)
    sleeve_id = models.ForeignKey("Sleeve",on_delete=models.CASCADE, null=True, blank=True)
    neck_id = models.ForeignKey("Neck",on_delete=models.CASCADE,null=True, blank=True)  
    price = models.BigIntegerField()
    seller_id = models.ForeignKey("home.Seller",on_delete=models.CASCADE,null=True)
    
class Album(models.Model):
    image =models.ImageField(upload_to='products/')
    product = models.ForeignKey("Products",on_delete=models.CASCADE)
    
class Category(models.Model):
    category_name = models.CharField(max_length=80)    
    
class Size(models.Model):
    size = models.CharField(max_length=50)  
    
class Material(models.Model):
    material = models.CharField(max_length=80)     
    
class Fit(models.Model):
    fit_type = models.CharField(max_length=100)     
    
class Pattern(models.Model):
    pattern = models.CharField(max_length=100) 
    
class Sleeve(models.Model):
    sleeve_type = models.CharField(max_length=130)    
    
class Neck(models.Model):
    neck_type = models.CharField(max_length=100)    
    
class Variant(models.Model):
    product_id = models.ForeignKey("Products", on_delete=models.CASCADE) 
    size_id = models.ForeignKey("Size", on_delete=models.CASCADE) 
    quantity = models.BigIntegerField()
        
