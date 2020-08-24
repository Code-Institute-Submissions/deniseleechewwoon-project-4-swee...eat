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
            'cost': float(product.price),
            'qty': 1
        }

        messages.success(
                request, f"Added '{product.name}' to the shopping cart")

    else:
        cart[product_id]['qty'] += 1

    request.session['shopping_cart'] = cart
    return redirect(reverse('view_product_route', args=(product_id,)))


def view_cart(request):
    cart = request.session.get('shopping_cart', {})

    total = 0
    for k, v in cart.items():
        cart[k]['total_cost'] = int(cart[k]['qty'])*float(cart[k]['cost'])
        total += float(v['cost']) * int(v['qty'])

    request.session["shopping_cart"] = cart

    return render(request, 'cart/view_cart.template.html', {
        "cart": cart,
        "total": total
    })


def remove_from_cart(request, product_id):
    cart = request.session["shopping_cart"]
    if product_id in cart:
        del cart[product_id]

        request.session['shopping_cart'] = cart

        messages.success(request, "The item has been removed")

    return redirect(reverse('view_cart'))


def update_quantity(request, product_id):
    cart = request.session["shopping_cart"]
    if product_id in cart:
        cart[product_id]['qty'] = request.POST['qty']

        request.session["shopping_cart"] = cart
        messages.success(
            request, f"Quantity for {cart[product_id]['name']} has been changed")

        return redirect(reverse('view_cart'))
    else:
        messages.success(request, "The products doesn't exist in your cart.")
        return redirect(reverse('view_cart'))

