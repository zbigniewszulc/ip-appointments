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