from django.db import models

class Client(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    regdate = models.DateTimeField(auto_now_add=True)

class Ware(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.CharField(max_length=100)
    regdate = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    uid = models.ForeignKey(Client, on_delete=models.CASCADE)
    wid = models.ManyToManyField
    bill = models.DecimalField(max_digits=8, decimal_places=2)
    regdate = models.DateTimeField(auto_now_add=True)

# Create your models here.
