from django.db import models
from products.models import Product

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=255, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    date = models.DateField(blank=False)

    def __str__(self):
        return self.title
