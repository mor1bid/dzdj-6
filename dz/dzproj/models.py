from django.db import models

class Client(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    adress = models.CharField()
    regdate = models.DateField()

class Ware(models.Model):
    name = models.TextField()
    descriprion = models.CharField()
    price = models.IntegerField()
    count = models.IntegerField()
    regdate = models.DateField()

class Order(models.Model):
    uid = models.ForeignKey(Client, on_delete=models.CASCADE)
    wid = models.ManyToManyField
    bill = models.IntegerField()
    regdate = models.DateField()

# Create your models here.
