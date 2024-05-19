from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    def __str__(self):
     return self.product_name
    category=models.CharField(max_length=50 ,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")



class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    desc=models.CharField(max_length=50)
    def __str__(self):
     return self.name


class Orders(models.Model):
    order_id=models.IntegerField()
    order_name=models.CharField(max_length=50)
    phone=models.IntegerField()
    desc=models.CharField(max_length=50)
    def __str__(self):
     return self.order_name
