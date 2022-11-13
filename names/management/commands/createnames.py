from django.core.management.base import BaseCommand
from names.models import Name


class Command(BaseCommand):
    help = "Create Superuser and some test names"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        Name.objects.all().delete()
        name_count = options['count']

        Name.objects.ccreate_superuser('Nik', 'nik@nik.com', '1'),

        # создаем тестовых пользователей
        for i in range(name_count):
            Name.objects.create_name(f'user{i}', f'user{i}@test.com', '1')
        print('done')
