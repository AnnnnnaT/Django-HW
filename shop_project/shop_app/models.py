from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_num = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    sign_up_date = models.DateField()

class Product(models.Model):
   name = models.CharField(max_length=50)
   description = models.TextField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
   number = models.IntegerField()
   product_added = models.DateField()
   image = models.ImageField(default=None)

class Order(models.Model):
   client = models.ForeignKey(Client, on_delete=models.CASCADE)
   products = models.ManyToManyField(Product)
   total_price = models.DecimalField(max_digits=10, decimal_places=2)
   order_date = models.DateField()

   def items(self):
      products = []
      for p in self.products:
         products.append(p.name)
      return products
 