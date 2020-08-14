from django.db import models


from django.core.validators import MinLengthValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=False, max_length=255, validators=[
                             MinLengthValidator(3)])
    description = models.TextField(blank=False)
    price = models.IntegerField(blank=False)

    def __str__(self):
        return self.name
