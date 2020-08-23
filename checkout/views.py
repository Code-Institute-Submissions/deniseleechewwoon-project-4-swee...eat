from django.shortcuts import render, get_object_or_404, HttpResponse, reverse
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt

# import in the settings
from django.conf import settings

# import in stripe
import stripe

# import in the product
from products.models import Product

# import in the purchase and user
from .models import Purchase
from django.contrib.auth.models import User


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
            "currency": "usd",
            "description": product_model.id
         }

        line_items.append(item)

    current_site = Site.objects.get_current()
    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        client_reference_id=request.user.id,
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


@csrf_exempt
def payment_completed(request):
    payload = request.body

    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    endpoint_secret = "whsec_Qu9MPpHB4MzEdu8IBP5pWmBYYrbWP6np"
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret)
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event['data']['object']

        handle_payment(session)

    return HttpResponse(status=200)


def handle_payment(session):
    user = get_object_or_404(User, pk=session["client_reference_id"])

    for line_item in session["display_items"]:
        product_id = int(line_item["custom"]["description"])
        product_model = get_object_or_404(Product, pk=product_id)

        # create the purchase model
        purchase = Purchase()
        purchase.product_id = product_model
        purchase.user_id = user
        purchase.save()

