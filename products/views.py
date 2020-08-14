from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Product
from .forms import ProductForm

# Create your views here.
def index(request):
    fname = "Denise"
    lname = "Lee"
    return render(request, 'products/index.template.html', {
        'first_name':fname,
        'last_name':lname
    })

def show_products(request):
    all_products = Product.objects.all()
    return render(request, 'products/all_products.template.html', {
        'products' : all_products
    })

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        form.save()
        return redirect(reverse(show_products))
    else:
        form = ProductForm()
        return render(request, 'products/create_product.template.html', {
            'form': form
    })