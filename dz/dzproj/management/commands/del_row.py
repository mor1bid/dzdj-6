from django.core.management.base import BaseCommand
from dzproj.models import Ware

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        ware = Ware.objects.filter(id=pk).first()
        if ware is not None:
            ware.delete()
            self.stdout.write("Запись удалена")
        else:
            self.stdout.write("Запись не существует")
        self.stdout.write(f"{ware}")
