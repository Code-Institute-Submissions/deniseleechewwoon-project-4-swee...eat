from django.contrib import admin
from django.urls import path, include
import products.views

urlpatterns = [
    path('', products.views.index),
    path('all',
         products.views.show_products, name='all_products_route'),
    path('create', products.views.create_product),
    path('details/<product_id>',
         products.views.view_product, name='view_product_route'),
    path('update/<product_id>',
         products.views.edit_product, name='update_product_route'),
    path('delete/<product_id>',
         products.views.delete_product, name='delete_product_route'),
]

