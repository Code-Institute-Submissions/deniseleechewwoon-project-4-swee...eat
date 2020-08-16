from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

# Create your views here.


def index(request):
    fname = "Denise"
    lname = "Lee"
    return render(request, 'products/index.template.html', {
        'first_name': fname,
        'last_name': lname
    })


def show_products(request):
    all_products = Product.objects.all()
    return render(request, 'products/all_products.template.html', {
        'products': all_products
    })

@login_required
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        form.save()

        messages.success(request, "New product has been added")

        return redirect(reverse(show_products))
    else:
        form = ProductForm()
        return render(request, 'products/create_product.template.html', {
            'form': form
        })

def view_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.template.html', {
        'product': product
    })

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        form.save()
        return redirect(reverse(show_products))
    else:
        form = ProductForm(instance=product)
        return render(request, 'products/edit_product.template.html', {
            'form': form,
            'product': product
        })

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        product.delete()
        return redirect(reverse(show_products))
    else:
        return render(request, 'products/confirm_delete_product.template.html', {
            'product': product
    })