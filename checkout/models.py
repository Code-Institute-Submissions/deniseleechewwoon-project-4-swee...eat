from django.db import models
from products.models import Product

from django.contrib.auth.models import User

# Create your models here.

class Delivery(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"Delivery to {self.street_address1} {self.street_address2} {self.postcode}, attn:{self.full_name}"


class Purchase(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    #delivery_id = models.ForeignKey('Delivery', on_delete=models.CASCADE)

    def __str__(self):
        return f"Purchase made for product#{self.product_id} by user#{self.user_id} on {self.purchase_date}"
