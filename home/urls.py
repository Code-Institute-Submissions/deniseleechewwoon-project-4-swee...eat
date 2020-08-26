from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('story', views.story, name='story'),
    path('contact', views.contact, name='contact')
]
