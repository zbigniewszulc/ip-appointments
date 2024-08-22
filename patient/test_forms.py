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

    def test_username_required(self):
        """Test the 'username' field"""
        patient_form = PatientSignupForm({
            'email': 'test@example.com',
            'username': '',
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
        self.assertFalse(
            patient_form.is_valid(),
            msg='Username was not provided, but the form is valid'
        )

    def test_phone_number_validation(self):
        """Test for valid and invalid phone numbers"""

        # Valid phone number
        patient_form = PatientSignupForm({
            'email': 'test@example.com',
            'username': 'testuser',
            'first_name': 'Mark',
            'last_name': 'Hennesy',
            'date_of_birth': '1990-02-01',
            'address_line_1': 'Apt 1 Pinewoods',
            'address_line_2': 'Clondalkin',
            'address_line_3': '',
            'phone_number': '0860860860',
            'password1': 'kjnkjdfnvdf72jd!2',
            'password2': 'kjnkjdfnvdf72jd!2'
        })
        self.assertTrue(
            patient_form.is_valid(), msg='Valid phone number was not accepted'
        )

        # Invalid phone number
        patient_form = PatientSignupForm({
            'email': 'test@example.com',
            'username': 'testuser',
            'first_name': 'Mark',
            'last_name': 'Hennesy',
            'date_of_birth': '1990-02-01',
            'address_line_1': 'Apt 1 Pinewoods',
            'address_line_2': 'Clondalkin',
            'address_line_3': '',
            'phone_number': 'invalidphone',
            'password1': 'kjnkjdfnvdf72jd!2',
            'password2': 'kjnkjdfnvdf72jd!2'
        })
        self.assertFalse(
            patient_form.is_valid(), msg='Invalid phone number was accepted'
        )