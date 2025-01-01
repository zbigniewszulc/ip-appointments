from django.shortcuts import render
from .forms import PatientSignupForm
from django.contrib.auth.decorators import login_required
from appointment.models import Appointment

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

@login_required
def my_appointments(request):
    """
    Display the logged-in patient's appointments.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML template containing patient's appointments.
        
    Template:
        `patient/my_appointments.html`

    Context:
        appointments (QuerySet): A list of the patient's appointments, 
            sorted by date and time slot
        message (str): A message indicating there are no appointments, 
            if applicable.
    """
    appointments = Appointment.objects.filter(
        patient=request.user.patient).order_by('-date', '-time_slot')
    
    # assign default message variable to none
    message = None 

    if not appointments:
        message = 'You have no appointments booked so far yet!' 

    return render(request, 'patient/my_appointments.html', 
        {'appointments': appointments, 'message': message})