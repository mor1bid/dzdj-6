from django.core.management.base import BaseCommand
from dzproj.models import *
from datetime import date
from faker import Faker
import random, sys

fake = Faker('ru_RU')

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print(sys.getsizeof(Client()))
        key = random.randint(0, sys.getsizeof(Client()))
        fuid = Client.objects.filter(id=key)
        fwid = Ware.objects.filter(id=key)
        fbill = Ware.price
        fdate = date.today()
        order = Orders(uid=fuid, wid=fwid, bill=fbill, regdate=fdate)
        order.save()
        self.stdout.write(f'{order}')