from django.test import TestCase
from .forms import PatientSignupForm


# Create your tests here.
class TestPatientSignupForm(TestCase):

    def test_form_is_valid(self):
        """Test whether form is valid """
        patient_form = PatientSignupForm({
            'email': 'test@test.com',
            'username': 'markhennesy',
            'first_name': 'Mark',
            'last_name': 'Hennesy',
            'date_of_birth': '1990-02-01',
            'address_line_1': 'Apt 1 Pinewoods',
            'address_line_2': 'Clodnalkin',
            'address_line_3': '',
            'phone_number': '0860860860',
            'password1': 'kjnkjdfnvdf72jd!2',
            'password2': 'kjnkjdfnvdf72jd!2'
        })
        self.assertTrue(patient_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self):
        """Test whether the form is invalid with empty fields"""
        patient_form = PatientSignupForm({
            'email': '',
            'username': '',
            'first_name': '',
            'last_name': '',
            'date_of_birth': '',
            'address_line_1': '',
            'address_line_2': '',
            'address_line_3': '',
            'phone_number': '',
            'password1': '',
            'password2': ''
        })
        self.assertFalse(
            patient_form.is_valid(), 
            msg='Form is valid despite missing data'
        )