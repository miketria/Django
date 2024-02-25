from django import forms
from my_app.models import Product
from django.forms import ModelForm

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["name","price","description"]      