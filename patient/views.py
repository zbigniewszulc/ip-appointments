from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Patient
from .forms import PatientSignupForm

# Create your views here.
def index(request):
    """ 
    Display the patient signup form. 

    **Context** 
    ``patient_signup_form`` 
    	An instance of :form:`PatientSignupForm`. 

    **Template:** 
    :template:`patient/index.html` 
    """
    patient_signup_form = PatientSignupForm()
    
    return render( 
        request, 
        "patient/index.html", 
        { 
            "patient_signup_form": patient_signup_form, 
        }, 
    )