from django.core.management.base import BaseCommand, CommandParser
from django.shortcuts import get_object_or_404
from dzproj.models import *
from datetime import date
from faker import Faker
import random

fake = Faker('ru_RU')

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('id', type=int, )
        parser.add_argument('ware', type=str, )
        parser.add_argument('price', type=int, )

    def handle(self, *args, **kwargs):
        myid = kwargs['id']
        myware = kwargs['ware']
        myprice = kwargs['price']
        client = Client.objects.get(pk=myid)
        user = client.name
        myprice = kwargs['price']
        fdate = date.today()
        if Ware.objects.filter(pk=myware) and Ware.objects.filter(pk=myprice):
            order = Orders(uid=user, wid=myware, bill=+myprice, regdate=fdate)
            order.save()
            self.stdout('Заказ добавлен')
        else:
            self.stdout('Произошла ошибка. Повторите ещё раз')
        self.stdout.write(f'{order}')