from django.core.management.base import BaseCommand
from shop_app.models import Client, Product, Order
from random import choice, randint, choices
import decimal


class Command(BaseCommand):
    help = "Create order"

    def handle(self, *args, **kwargs):

        clients = Client.objects.all()
        products = Product.objects.all() #список 

        for i in range(10):
            order = Order(
                client = choice(clients),
                total_price = sum(p.price for p in products),
                # decimal.Decimal('%d.%d' % (randint(0,1000), randint(0,100)))
                order_date = f'2000-01-{randint(1,30)}',
            )
            order.save() #сохраняем заказ в БД
            products_ = choices(products, k=randint(1,10))
            for product in products_:
                order.products.add(product)
        self.stdout.write(f'created {Order.objects.count()} orders')