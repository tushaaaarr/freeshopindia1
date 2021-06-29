from django.db import models


# Create your models here.

class Product(models.Model):    
    product_id=models.AutoField
    product_name=models.CharField(max_length=500)
    category= models.CharField(max_length=50)
    sub_category= models.CharField(max_length=50)
    price=models.IntegerField(max_length = 200)
    # desc=models.CharField(max_length=300)
    # long_desc= models.CharField(max_length = 500)
    pub_date=models.DateField()
    img_url1 = models.CharField(max_length = 500)
    brand = models.CharField(max_length= 100)
    # img_url2 = models.CharField(max_length = 500)
    # img_url3 = models.CharField(max_length = 500)
    # image= models.ImageField(upload_to="'shop/images'")
    # image2= models.ImageField(upload_to="'shop/images'")
    def __str__(self):
        return self.product_name


class New_Product2(models.Model):  
    query = models.CharField(max_length=500)

    # product_name=models.CharField(max_length=500)
    # price=models.IntegerField()
    # category= models.CharField(max_length=50)
    # sub_category= models.CharField(max_length=50)
    # img_url1 = models.CharField(max_length = 500)
    # pub_date=models.DateField()
    def __str__(self):
        return self.query



class Mobile(models.Model):
    product_name = models.CharField(max_length=50)
    Display= models.CharField(max_length=50)
    front_cam =  models.CharField(max_length=50)
    rear_cam = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    storage= models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    def __str__(self):
        return self.product_name

class Laptop(models.Model):
    product_name = models.CharField(max_length=50)
    Display= models.CharField(max_length=50)
    Operating_System =  models.CharField(max_length=50)
    CPU = models.CharField(max_length=50)
    Screen = models.CharField(max_length=50)
    Processor = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    Memory  = models.CharField(max_length=50)
    def __str__(self):
        return self.product_name


class Searched_item(models.Model):
    query = models.CharField(max_length=400)
    
    def __str__(self):
        return self.product_name
