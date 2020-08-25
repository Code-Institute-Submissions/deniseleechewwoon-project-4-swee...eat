from django.contrib import admin
from .models import Delivery
from .models import Purchase

# Register your models here.
admin.site.register(Delivery)
admin.site.register(Purchase)
