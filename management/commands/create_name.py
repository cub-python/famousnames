from django.core.management.base import BaseCommand
from famousnames.names.models import Name

class Command(BaseCommand):
    def handle(self, *args, **options):

        Name.objects.create(first_name='test',last_name='test')