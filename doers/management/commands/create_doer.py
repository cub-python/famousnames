from django.contrib.auth.models import User
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    def handle(self, *args, **options):
        # Doer.objects.create(first_name='test', last_name='test', birthday_year=1111)
        User.objects.create_superuser(username='nikola', password='1', email='test@bk.ru')


