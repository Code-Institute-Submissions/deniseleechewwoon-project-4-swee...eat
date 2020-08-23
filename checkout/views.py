from django.shortcuts import render, get_object_or_404, HttpResponse, reverse
from django.contrib.sites.models import Site

# import in the settings
from django.conf import settings

# import in stripe
import stripe

# import in the product
from products.models import Product


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('shopping_cart', {})

    line_items = []
    
    for product_id, product in cart.items():
        product_model = get_object_or_404(Product, pk=product_id)

        item = {
            "name": product_model.name,
            "amount": int(product_model.price * 100),
            "quantity": product['qty'],
            "currency": "usd"
         }
        
        line_items.append(item)
    
    current_site = Site.objects.get_current()
    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # take credit cards
        line_items=line_items,
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, 'checkout/checkout.template.html', {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_success(request):
    return HttpResponse("checkout success")


def checkout_cancelled(request):
    return HttpResponse("checkout cancelled")
