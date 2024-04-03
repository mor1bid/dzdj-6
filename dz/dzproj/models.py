from django.db import models
from django_tables2 import tables, LinkColumn
from django_tables2.utils import Accessor

class Client(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    regdate = models.DateTimeField(auto_now_add=True)

class Ware(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='media', storage='media')
    name = models.TextField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.CharField(max_length=100)
    regdate = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(ware.price for ware in Ware.objects.all())

class Orders(models.Model):
    uid = LinkColumn('dz:dzproj_client', args=[Accessor('pk')])
    uid = models.TextField(default= '')
    wid = LinkColumn('dz:dzproj_ware', args=[Accessor('pk')])
    wid = models.TextField(default= '')
    bill = models.DecimalField(max_digits=8, decimal_places=2)
    regdate = models.DateField()

    def __str__(self):
        return f'{self.uid}, {self.wid}, {self.bill}'
    
class OrdersMem(models.Model):
    uid = models.TextField(default= '')
    wid = models.TextField(default= '')
    regdate = models.DateField()

# Create your models here.
