from django.urls import path
from . import views

urlpatterns = [
    path('products/<str:product_name>/', views.print_all_products, name='product_list'),
    path('products/<str:product_name>/', views.product_details, name='product_details'),
    path('add_product/', views.add_product, name='add_product')
]