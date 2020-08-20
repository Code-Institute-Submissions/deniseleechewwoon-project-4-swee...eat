from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def add_to_cart(request, product_id):
    cart = request.session.get('shopping_cart', {})

    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)

        cart[product_id] = {
            'id': product_id,
            'name': product.name,
            'cost': 99,
            'qty': 1
        }

    else:
        cart[product_id]['qty'] += 1

    request.session['shopping_cart'] = cart
    return HttpResponse("product added")


def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    return render(request, 'cart/view_cart.template.html', {
        "cart": cart
    })