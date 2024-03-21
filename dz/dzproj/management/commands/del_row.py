from django.core.management.base import BaseCommand
from dzproj.models import *

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        # parser.add_argument('classn', type=classmethod, help='Models name')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        ware = Orders.objects.filter(pk=pk).first()
        if ware is not None:
            ware.delete()
            self.stdout.write("Запись удалена")
        else:
            self.stdout.write("Запись не существует")
        self.stdout.write(f"{ware}")
