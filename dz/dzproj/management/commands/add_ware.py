from django.core.management.base import BaseCommand
from dzproj.models import Ware
from datetime import date
from faker import Faker
import random

fake = Faker('ru_RU')

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        wareslist = ["Продовольствие", "Медикаменты", "Техника", "Роскошь", "Минералы", "Алкоголь", "Оружие", "Наркотики"]
        key = random.randint(0, len(wareslist)-1)
        fname = wareslist[key]
        fdesc = "A qualified ware. Buy it."
        fprice = random.randint(0, 500)
        fcount = str(random.randint(0, 1000)) + ' pcs'
        fdate = date.today()
        ware = Ware(name=fname, description=fdesc, price=fprice, count=fcount, regdate=fdate)
        ware.save()
        self.stdout.write(f'{ware}')