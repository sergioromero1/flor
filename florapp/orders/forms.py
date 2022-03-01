# django
from django import forms

# models

from orders.models import Order

class OrderForm(forms.ModelForm):
    """Order model form"""

    class Meta:
        """Form settings"""

        model = Order
        fields = ['units', 'unit_price', 'observations_text']