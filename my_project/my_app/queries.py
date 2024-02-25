from django.shortcuts import render
from my_app.models import Product
  
products_over_100=Product.objects.filter(price__gt=100)

top_5_products=Product.objects.order_by("-price")[:5]

new_price = 10.00
product_to_update=Product.objects.filter(name='first product')
product_to_update.update(price=new_price)