from django.test import TestCase
from .forms import BookAppointmentForm
from .models import Service

# Create your tests here.
class TestBookAppointmentForm(TestCase):

    def setUp(self):
        """ Create sample service """
        self.service = Service.objects.create(name="General Dentistry")
        
    def test_form_is_valid(self):
        """ Test whether form is valid """
        appointment_form = BookAppointmentForm({
            'service': self.service.id,
            'date': '2024-08-22', 
            'time_slot': '14:00'
        })
        self.assertTrue(appointment_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        """ Test whether form is invalid """
        appointment_form = BookAppointmentForm({
            'service': '',
            'date': '', 
            'time_slot': ''
        })
        self.assertFalse(appointment_form.is_valid(), msg='Form is valid')

    def test_service_required(self):
        """ Test for 'service' field """
        appointment_form = BookAppointmentForm({
            'service': '',
            'date': '2024-08-22', 
            'time_slot': '14:00'
        })
        self.assertFalse(
            appointment_form.is_valid(), 
            msg='Service was not provided, but the form is valid'
        )
