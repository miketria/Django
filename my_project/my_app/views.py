from django.shortcuts import render, get_object_or_404, redirect
from my_app.models import Product
from my_app.form import ProductForm

# Create your views here.
def print_all_products(request):
    products=Product.objects.all()
    context={'products': products}
    return render(request, 'product_list.html', context)

def product_details(request, product_name):
    product=get_object_or_404(Product, name=product_name)
    context={'product': product}
    return render(request, 'product_list.html', context)

def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form=ProductForm()
    return render(request, 'add_product.html', {'form': form})