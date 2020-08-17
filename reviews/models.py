from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=255, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    date = models.DateField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
