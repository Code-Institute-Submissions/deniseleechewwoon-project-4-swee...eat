from django import forms
from .models import Product, Tags, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'tags')


class SearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False)
    price_below = forms.IntegerField(required=False)
