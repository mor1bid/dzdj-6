from django.core.management.base import BaseCommand
from dzproj.models import *
from datetime import date
from faker import Faker
import random

fake = Faker('ru_RU')

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        ukey = random.randint(1, Client.objects.count())
        fuid = Client.objects.get(id=ukey)
        wkey = random.randint(1, Ware.objects.count())
        fwid = Ware.objects.get(id=wkey)
        fbill = Ware.objects.get(name=fwid)
        fdate = date.today()
        order = Orders(uid=fuid, wid=fwid, bill=fbill, regdate=fdate)
        order.save()
        self.stdout.write(f'{order}')