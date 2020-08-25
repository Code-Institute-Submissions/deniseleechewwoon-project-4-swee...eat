from .models import Delivery
from django import forms

class OrderForm(forms.ModelForm):
    #user_id=forms.CharField(widget=forms.HiddenInput)
    class Meta:
        model = Delivery
        fields = (
            'full_name', 'phone_number', 'country', 'town_or_city', 'street_address1', 'street_address2', 'postcode'
        )
