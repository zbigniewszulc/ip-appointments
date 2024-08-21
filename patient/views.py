from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Patient
from .forms import PatientSignupForm

# Create your views here.
def index(request):
    """
    Display the patient signup form.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML template containing patient signup form.

    Template:
        `patient/index.html`

    Context:
        patient_signup_form (PatientSignupForm): Instance of PatientSignupForm.
    """
    patient_signup_form = PatientSignupForm()
    
    return render( 
        request, 
        "patient/index.html", 
        { 
            "patient_signup_form": patient_signup_form, 
        }, 
    )