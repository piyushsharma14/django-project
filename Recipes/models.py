from django.db import models

 # Create your models here.
class recipes(models.Model):
    Date= models.CharField(max_length=40)
    Recipe_name= models.CharField(max_length=200)
    Recipe_image = models.ImageField(upload_to='media',null=True,blank=True)
    content_image = models.ImageField(upload_to='media',null=True,blank=True)
    Prep_time = models.CharField(max_length=40,default=1)
    Cook_time = models.CharField(max_length=40,default=1)
    Heading_first = models.CharField(max_length=100,default=1,blank=True)
    content_first = models.TextField(max_length=300,default=1,blank=True)
    Heading_second = models.CharField(max_length=100,default=1,blank=True)
    content_second = models.TextField(max_length=300,default=1,blank=True)
    Heading_third = models.CharField(max_length=100,default=1,blank=True)
    content_third = models.TextField(max_length=300,default=1,blank=True)
    Key_Ingredients = models.TextField(max_length=300,default=1,blank=True)
    Ingredients_content_one = models.TextField(max_length=200,default=1,blank=True)
    Ingredients_content_two = models.TextField(max_length=200,default=1,blank=True)
    Ingredients_content_three = models.TextField(max_length=200,default=1,blank=True)
    Ingredients_content_four = models.TextField(max_length=200,default=1,blank=True)
    Ingredients_content_five = models.TextField(max_length=200,default=1,blank=True)

class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=200)
