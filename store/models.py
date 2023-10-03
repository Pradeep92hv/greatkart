from django.db import models

# Create your models here.

from category.models import Category
class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug        =models.SlugField(max_length=300,unique=True)
    description =models.TextField(max_length=500,blank=True)
    price       =models.IntegerField()
    image       =models.ImageField(upload_to='photos/products')
    stock       =models.IntegerField()
    is_available=models.BooleanField(default=True)
    category    =models.ForeignKey(Category,on_delete=models.CASCADE)
    created_data=models.DateTimeField(auto_now_add=True)
    modified    =models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.product_name
   
variation_category_choice=(
       ('color','color'),
       ('size','size'),
   ) 
    
class variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100,choices=variation_category_choice)  # dropdown for color , size in adminpanel
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date =models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.product