from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product, Category, Tags
from django.contrib import messages
from django.db.models import Q
from reviews.models import Review
# Create your views here.


def index(request):
    return render(request, 'home/index.template.html')

def story(request):
    return render(request, 'home/story.template.html')

def contact(request):
    return render(request, 'home/contact.template.html')
