from django.db import models
from cloudinary.models import CloudinaryField


from django.core.validators import MinLengthValidator

# Create your models here.
class Tags(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(blank=False, max_length=255, validators=[
                             MinLengthValidator(3)])
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    cover = CloudinaryField()

    def __str__(self):
        return self.name
