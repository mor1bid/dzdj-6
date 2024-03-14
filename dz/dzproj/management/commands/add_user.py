from django.core.management.base import BaseCommand
from dzproj.models import Client
from datetime import date
from faker import Faker

fake = Faker('ru_RU')

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fname = fake.name()
        femail = fake.email()
        fphone = fake.phone_number()
        faddress = fake.address()
        fdate = date.today()
        user = Client(name=fname, email=femail, phone=fphone, address=faddress, regdate=fdate)
        user.save()
        self.stdout.write(f'{user}')