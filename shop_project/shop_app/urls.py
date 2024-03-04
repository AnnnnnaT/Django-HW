from django.urls import path
from shop_app import views

urlpatterns = [
    path('orders/<int:client_id>/', views.orders_by, name='orders_by'), 
    path('products/<int:client_id>/', views.products_by_date, name='products_by_date'), 
    path('product_edit/<int:product_id>/', views.product_edit, name='product_edit'), 
]