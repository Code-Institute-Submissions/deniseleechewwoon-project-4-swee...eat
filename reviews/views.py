from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from products.models import Product
from .models import Review

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

def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        form.save()
        messages.success(request, "Review has been edited")
        return redirect(reverse(index))

    else:
        form = ReviewForm(instance=review)
        return render(request, 'reviews/edit_review.template.html', {
            'form': form,
            'review': review
        })

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        review.delete()
        return redirect(reverse(index))
    else:
        return render(request, 'reviews/confirm_delete_review.template.html', {
            'review': review
    })