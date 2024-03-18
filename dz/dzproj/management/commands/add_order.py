from django.core.management.base import BaseCommand, CommandParser
from django.shortcuts import get_object_or_404
from dzproj.models import *
from datetime import date
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
        fdate = date.today()
        waresize = Ware.objects.count()
        wname = Ware._meta.get_field('name')
        wprice = Ware._meta.get_field('price')
        for w in range(1, waresize):
            obj = Ware.objects.get(pk=w)
            ware = getattr(obj, wname.attname)
            price = getattr(obj, wprice.attname)
            if myware == ware and myprice == price:
                order = Orders(uid= myid, wid=w, bill=+myprice, regdate=fdate)
                order.save()
                self.stdout.write('Заказ добавлен')
                return 0
            # else:
            #     self.stdout('Произошла ошибка. Повторите ещё раз')
            # self.stdout.write(f'{order}')