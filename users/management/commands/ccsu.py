from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='89365265993@mail.ru',
            first_name='Petr',
            last_name='Ivanov',
            is_superuser=True,
            is_staff=True,
            is_active=True,

        )

        user.set_password('12345qwerty')
        user.save()
