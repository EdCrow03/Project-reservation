from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table_type', 'reservation_date', 'number_of_guests', 'reservation_time', 'message', 'status']