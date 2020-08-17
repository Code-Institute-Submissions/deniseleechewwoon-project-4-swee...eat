from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from products.models import Product

# Create your views here.
def index(request):
    return render(request, 'reviews/index.template.html')

def create_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product

            review.save()
            messages.success(request, "New review has been added")
            #return HttpResponse("Review is created")
            return render(request, 'products/details.template.html', {
            'product': product
             })
        else:
            return HttpResponse("Form has error")
    else:
        form = ReviewForm()
        return render(request, 'reviews/create_review.template.html', {
                "form": form,
                "product": product
        })
