from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientSignupForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from appointment.models import Appointment
from django.contrib import messages
from .models import Patient

# Create your views here.


def index(request):
    """
    Display the patient signup form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML template containing the patient signup form.

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


@login_required
def cancel_appointment(request, appointment_id):
    """
    Cancel an appointment for the logged-in patient.

    Args:
        request (HttpRequest): The HTTP request object.
        appointment_id (int): The ID of the appointment to be canceled.

    Returns:
        HttpResponseRedirect: Redirects to the `my_appointments` page 
        after cancellation.

    Template:
        `patient/my_appointments.html`

    Context:
        Redirects after canceling - no context
    """
    appointment = get_object_or_404(
        Appointment, id=appointment_id, patient=request.user.patient)

    if request.method == 'POST':
        appointment.delete()

        # Send confirmation email to the patient
        subject = 'Appointment Cancellation Confirmation'
        message = (
            f'Dear {request.user.first_name},\n\n'
            f'Your appointment for {appointment.service.name} '
            f'on {appointment.date} at {appointment.time_slot} '
            'has been successfully cancelled.\n\n'
            'Thank you for using our booking system.\n\n'
            'Best Regards,\nInfinita Perfectio'
        )
        
        try:
            send_mail(
                subject, message, settings.DEFAULT_FROM_EMAIL, 
                [request.user.email])
        except Exception as e:
            # Log error if occured
            print(f"Error sending email for appointment cancellation: {e}")

        # Add success message 
        messages.success(
            request, 'Your appointment has been successfully canceled.')

        return redirect('my_appointments')
    
    # In case if there was error cancelling appointment
    messages.error(
        request, 'Failed to cancel the appointment. Please try again.')

    return redirect('my_appointments')


@login_required
def my_details(request):
    """
    View personal details of the logged-in patient.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders `my_details` template with the patient's details.

    Template:
        `patient/my_details.html`

    Context:
        patient (Patient): The details of the logged-in patient.
    """
    patient = get_object_or_404(Patient, user=request.user)
    context ={
        'patient' : patient
    }
    return render(request, 'patient/my_details.html', context)
