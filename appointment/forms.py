from django import forms
from .models import Appointment

class BookAppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ['date', 'time_slot', 'service']