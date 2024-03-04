from django.core.management.base import BaseCommand
from shop_app.models import Client, Product, Order
from django.utils import lorem_ipsum
from random import choice, randint, choices
import decimal

class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **kwargs):

        for i in range(10):
            product = Product(
                name = f'Product_{i}',
                description = '\n'.join(lorem_ipsum.paragraphs(4)),
                price = decimal.Decimal('%d.%d' % (randint(100, 10000), randint(0,100))),
                number = randint(1,30),
                product_added = f'2001-0{randint(1,9)}-{randint(1,30)}',
                image = None
            )
            product.save()
        self.stdout.write(f'created {Product.objects.count()} products')