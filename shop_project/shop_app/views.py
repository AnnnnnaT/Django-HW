from django.shortcuts import render
from shop_app.models import Client, Product, Order
import datetime

start_time = datetime.datetime(2023, 5, 2, 12, 0, 0)
current_time = datetime.datetime.now()
time_passed = current_time - start_time

def orders_by(request, client_id):
    orders = Order.objects.filter(client_id = client_id)
    return render(request, 'shop_app/client_orders.html',  {'orders': orders})

def products_by_date(request, client_id):
    orders = Order.objects.filter(client_id = client_id)
    week = []
    month = []
    year = []
    products = {
        "for_last_week": week,
        "for_last_month": month,
        "for_last_year": year
    }
    for order in orders:
        if order.order_date - datetime.datetime.now() < 7 or order.order_date - datetime.datetime.now() == 7:
            for p in order.items:
                week.append(p)
        if order.order_date - datetime.datetime.now() < 31 or order.order_date - datetime.datetime.now() == 31:
            for p in order.items:
                if not p in week:
                    month.append(p)
        if order.order_date - datetime.datetime.now() < 365 or order.order_date - datetime.datetime.now() == 365:
            for p in order.items:
               if not p in week and not p in month:
                    year.append(p)               
    return render(request, 'shop_app/products_in_order.html', products)