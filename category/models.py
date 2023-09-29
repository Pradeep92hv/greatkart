from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.CharField(max_length=500,unique=True)
    discription=models.TextField(max_length=300,blank=True)
    cat_image=models.ImageField(upload_to='photos.category',blank=True)
    
    
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
    
    def __self__(self):
        return self.category_name
