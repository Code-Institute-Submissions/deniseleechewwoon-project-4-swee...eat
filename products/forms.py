from django import forms
from .models import Product, Tags, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'tags')
