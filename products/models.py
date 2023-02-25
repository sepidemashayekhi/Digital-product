from django.db import models
from django.utils import timezone

class Category(models.Model):
    parent =models.ForeignKey('self' , verbose_name='parents' , blank=True , null=True , on_delete=models.CASCADE)


    title = models.CharField(verbose_name='name' , max_length=50)
    caption = models.TextField(verbose_name='caption' , blank=True)
    avatar = models.ImageField(verbose_name='ImagePro' ,blank=True, upload_to='CategoryImage/')
    published_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_time']
        indexes = [
            models.Index(fields=['-published_time']),] 
        
        db_table = 'categories'
        verbose_name= 'Category'


        

    def __str__(self):
        return  self.title

    
class Product(models.Model):

    title = models.CharField(verbose_name='Name' , max_length=50)
    category=models.ManyToManyField('Category' , verbose_name='categories' , blank=True)

    caption = models.TextField(verbose_name='caption' ,blank=True)
    avatar = models.ImageField('ProImage' , upload_to='Products/')
    published_time = models.DateTimeField(auto_now_add=True)
    update_time= models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_time']
        indexes = [
            models.Index(fields=['-published_time']),] 
        
        db_table = 'products'
        verbose_name= 'product'


        

    def __str__(self):
        return  self.title




class File(models.Model):
    product = models.ForeignKey('Product' , on_delete=models.CASCADE )
    title = models.CharField(max_length=50)
    file = models.FileField(verbose_name='file' , upload_to='file/%Y/%M/&D/')
    published_time = models.DateTimeField(auto_now_add=True)
    update_time= models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_time']
        indexes = [
            models.Index(fields=['-published_time']),] 
        
        db_table = 'files'
        verbose_name= 'file'


        

    def __str__(self):
        return  self.title