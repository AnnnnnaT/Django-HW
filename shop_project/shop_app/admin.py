from django.contrib import admin
from .models import Client, Product, Order

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_num", "address", "sign_up_date"]
    list_filter = ["sign_up_date"]
    fieldsets = (("основная информация о клиенте",
                   {"fields": ["name", "email", "phone_num"], 
                                    "description": "контактные данные клиента",}),
                 ("дополнительная информация", {"fields":["address", "sign_up_date"]}),) #кортеж кортежей
    readonly_fields = ["sign_up_date"]

@admin.register(Product)
class PoroductAdmin(admin.ModelAdmin):
    list_display = ["name", "number", "price", "product_added"]
    list_filter = ["price", "product_added"]
    fieldsets = (("основная информация о товаре",
                   {"fields": ["name", "price", "number"]}),
                 ("дополнительная информация", {"fields":["description", "image", "product_added"]}),) 
    readonly_fields = ["name", "product_added"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["client", "total_price", "order_date"]
    list_filter = ["client", "order_date"]
    fieldsets = (("основная информация о заказе",
                   {"fields": ["client",  "total_price", "order_date"]}),
                 ("дополнительная информация", {"fields":["products"]}),) 
    readonly_fields = ["client", "order_date"]