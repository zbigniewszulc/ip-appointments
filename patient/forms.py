from allauth.account.forms import SignupForm
from django import forms
from .models import Patient
from django.core.validators import RegexValidator
from django.contrib import messages

# Formula for number phone validation. Using built-in regex validator.
phone_regex = RegexValidator( 
    regex=r'^\+?[0-9]{9,15}$', 
    message=('Invalid phone number. '
        'Accepted formats .e.g.: 0800123123 or with prefix +353800123123'
    )
)

# Custom Signup Form
class PatientSignupForm(SignupForm):
    username = forms.CharField(min_length=5, max_length=150, required=True)
    first_name = forms.CharField(min_length=2, max_length=150, required=True)
    last_name = forms.CharField(min_length=2, max_length=150, required=True)
    date_of_birth = forms.DateField(
        required=True, 
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    address_line_1 = forms.CharField(min_length=2,max_length=100, required=True)
    address_line_2 = forms.CharField(min_length=2,max_length=100, required=True)
    address_line_3 = forms.CharField(max_length=100, required=False)
    phone_number = forms.CharField(min_length=9, max_length=15, 
        required=True, validators=[phone_regex])

    # Override save() method to customize form saving process 
    def save(self, request):
        # Call save() method from parent class 
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        patient = Patient(
            user=user,
            # Store cleaned data (after validation)
            date_of_birth=self.cleaned_data['date_of_birth'],
            address_line_1=self.cleaned_data['address_line_1'],
            address_line_2=self.cleaned_data['address_line_2'],
            address_line_3=self.cleaned_data['address_line_3'],
            phone_number=self.cleaned_data['phone_number']
        )
        patient.save()
        messages.success(request, 'You account has been successfully created.')
        return user