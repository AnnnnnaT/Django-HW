from django.core.management.base import BaseCommand
from shop_app.models import Client
from random import choice, randint

class Command(BaseCommand):
    help = "Create clients"

    def handle(self, *args, **kwargs):

        nums = [randint(0,9) for i in range(11)]

        for i in range(10):
            client = Client(
                name = f'Client_{i}',
                email = f'Client_{i}@mail.ru',
                phone_num = f'{"".join(*nums)}',
                address = f"Adress_{i}",
                sign_up_date = f'2024-01-{randint(10,30)}'
            )
            client.save()
            self.stdout.write(f'{client.name}')
            