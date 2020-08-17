from django.shortcuts import render, HttpResponse
from .forms import ReviewForm

# Create your views here.
def index(request):
    return render(request, 'reviews/index.template.html')

def create_review(request):
    form = ReviewForm()
    return render(request, 'reviews/create_review.template.html', {
            "form": form
    })

