from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:client_id>/', views.orders_by, name='orders_by'), 
    path('products/<int:client_id>/', views.products_by_date, name='products_by_date'), 
]