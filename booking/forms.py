

from django import forms
from .models import Booking  # Corrected from 'booking' to 'Booking'

class BookingForm(forms.ModelForm):  # Corrected from 'bookingForm' to 'BookingForm'
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'user', 'package']  # Ensure 'package' matches the field name in the model

