from django.shortcuts import render
from shop_app.models import Client, Product, Order
import datetime
from .forms import ProductForm
from flask import redirect
from django.core.files.storage import FileSystemStorage


start_time = datetime.datetime(2023, 5, 2, 12, 0, 0)
current_time = datetime.datetime.now()
time_passed = current_time - start_time


def product_edit(request, product_id = None):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Product.objects.update(
                name = data['name'],
                description = data['description'],
                price = data['price'],
                number = data['number'],
                product_added = data['product_added'],
            )
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            form.save()
            return redirect("product_item")                        
    else:
        if product_id:
            form = ProductForm(instanse=product)
    return render(request, "blog/product_item.html", {"form": form})

def orders_by(request, client_id):
    orders = Order.objects.filter(client_id = client_id)
    return render(request, 'shop_app/client_orders.html',  {'orders': orders})

def products_by_date(request, client_id):
    # orders = Order.objects.filter(client_id = client_id)
    # week = []
    # month = []
    # year = []
    products = {
        "for_last_week": last_week_orders,
        "for_last_month": last_month_orders,
        "for_last_year": last_year_orders
    }

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    last_week_orders = Product.objects.filter(order__client=client_id,
                                               order__order_date__gte=last_week).distinct() 
    last_month = datetime.date.today() - datetime.timedelta(days=31)
    last_month_orders = Product.objects.filter(order__client=client_id,
                                               order__order_date__gte=last_month).distinct()
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    last_year_orders = Product.objects.filter(order__client=client_id,
                                               order__order_date__gte=last_year).distinct() 

    # for order in orders:
    #     if order.order_date - datetime.datetime.now() < 7 or order.order_date - datetime.datetime.now() == 7:
    #         for p in order.items:
    #             week.append(p)
    #     if order.order_date - datetime.datetime.now() < 31 or order.order_date - datetime.datetime.now() == 31:
    #         for p in order.items:
    #             if not p in week:
    #                 month.append(p)
    #     if order.order_date - datetime.datetime.now() < 365 or order.order_date - datetime.datetime.now() == 365:
    #         for p in order.items:
    #            if not p in week and not p in month:
    #                 year.append(p)               
    return render(request, 'shop_app/products_in_order.html', products)