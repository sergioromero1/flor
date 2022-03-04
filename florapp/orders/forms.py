# django
from django import forms

# models

from orders.models import Flower, Order

class OrderForm(forms.ModelForm):
    """Order model form"""

    class Meta:
        """Form settings"""

        model = Order
        fields = ['flower','units', 'observations_text']

    units = forms.IntegerField()
    observations_text = forms.CharField()

    flower = forms.ModelChoiceField(
        queryset = Flower.objects.all(), 
        empty_label = None,
    )
