from django import forms
from .models import Appointment, Service


class BookAppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['date', 'time_slot', 'service']


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['name']
