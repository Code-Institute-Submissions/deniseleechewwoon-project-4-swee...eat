from django.shortcuts import render, get_object_or_404, HttpResponse, reverse, redirect
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# import in the settings
from django.conf import settings

# import in stripe
import stripe

# import in the product
from products.models import Product

#import in OrderForm
from .forms import OrderForm

# import in the purchase and user
from .models import Purchase
from .models import Delivery
from django.contrib.auth.models import User


def create_delivery(request):
    if request.method == "POST":
        print(request.POST)
        form = OrderForm(request.POST)
    

        if form.is_valid():
            form.save()
            #delivery = form.save()
            #delivery.user_id = request.user.id
            #delivery.save()
            messages.success(request, "Delivery details has has been added")
            return redirect(reverse(checkout))
            

        else:
            return render(request, 'checkout/create_delivery.template.html', {
                'form': form
            })

    else:
        form = OrderForm(initial={"user_id":request.user.id})
        return render(request, 'checkout/create_delivery.template.html', {
                'form': form
            })


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('shopping_cart', {})

    line_items = []

    all_product_ids = []

    for product_id, product in cart.items():
        product_model = get_object_or_404(Product, pk=product_id)

        item = {
            "name": product_model.name,
            "amount": int(product_model.price * 100),
            "quantity": product['qty'],
            "currency": "usd"
         }

        line_items.append(item)
        all_product_ids.append(str(product_model.id))

    current_site = Site.objects.get_current()
    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        metadata={'all_products_id': ",".join(all_product_ids)},
        client_reference_id=request.user.id,
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, "checkout/checkout.template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_success(request):
    request.session["shopping_cart"] = {}
    messages.success(request, "Your purchases has been completed")
    return redirect(reverse('all_products_route'))


def checkout_cancelled(request):
    return HttpResponse("checkout cancelled")


@csrf_exempt
def payment_completed(request):
    payload = request.body

    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    endpoint_secret = settings.SIGNING_SECRET
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
    all_product_ids = session['metadata']['all_products_id'].split(",")

    for product_id in all_product_ids:
        product_model = get_object_or_404(Product, pk=product_id)

    delivery = Delivery.objects.get(user_id=user, linked=False)


    # create the purchase model
    purchase = Purchase()
    purchase.product_id = product_model
    purchase.user_id = user
    purchase.delivery_id = delivery
    delivery.linked = True
    delivery.save()
    purchase.save()
