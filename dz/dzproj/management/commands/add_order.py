from django.core.management.base import BaseCommand, CommandParser
from django.shortcuts import get_object_or_404
from dzproj.models import *
from datetime import datetime
from faker import Faker
import random


fake = Faker('ru_RU')

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Client id')
        parser.add_argument('ware', type=str, help='Ware name')
        parser.add_argument('price', type=int, help='Ware price')

    def handle(self, *args, **kwargs):
        myid = kwargs['id']
        myware = kwargs['ware']
        myprice = kwargs['price']
        myprice = kwargs['price']
        fdate = datetime.now().date()
        waresize = Ware.objects.count()
        uname = Client._meta.get_field('name')
        hmn = Client.objects.get(pk=myid)
        name = getattr(hmn, uname.attname)
        wname = Ware._meta.get_field('name')
        wprice = Ware._meta.get_field('price')
        for w in range(1, waresize+1):
            obj = Ware.objects.get(pk=w)
            ware = getattr(obj, wname.attname)
            price = getattr(obj, wprice.attname)
            if Orders.objects.filter(pk=myid).exists() and myware == ware and myprice == price:
                order = Orders.objects.get(pk=myid)
                order.wid += ', ' + str(ware)
                order.bill += myprice
                order.regdate = '2024-03-14'
                order.save()
                self.stdout.write('Заказ добавлен к существующему')
                return 0
            elif myware == ware and myprice == price:
                order = Orders(uid = name, wid = myware, bill = myprice, regdate = '2024-02-21')
                order.save()
                self.stdout.write(f"Заказ добавлен. Номер вашего заказа: {getattr(Orders.objects.latest('id'), Orders._meta.get_field('id').attname)}")
                return 0
            if w==waresize:
                self.stdout.write('Произошла ошибка. Ваш заказ не был оформлен.')