from django.test import TestCase
from django.urls import reverse
from .models import Service, Appointment
from patient.models import Patient
from django.contrib.auth.models import User
from datetime import datetime

class TestCalendarView(TestCase):

    def setUp(self):
        # Create a service
        self.service = Service.objects.create(name="General Dentistry")

        # Create sample user and log in
        self.user = User.objects.create_user(
            username = 'TestUser',
            password = 'SamplePassword123',
            first_name = 'Test', 
            last_name = 'User',
            email = 'test@test.com'
        )
        self.client.login(username='TestUser', password='SamplePassword123')

        # Create sample patient
        self.patient = Patient.objects.create(
            user = self.user, 
            date_of_birth = '1999-01-02',
            address_line_1 = '123 Pinewoods Drive',
            address_line_2 = 'Clondalkin',
            address_line_3 = '',
            phone_number='0860860860'
        )

        # Create sample appointment
        self.appointment_date = datetime.strptime(
            '2024-08-19', '%Y-%m-%d').date()
        self.appointment_slot = datetime.strptime('14:00', '%H:%M').time()

        self.appointment = Appointment.objects.create(
            patient = self.patient, 
            service = self.service,
            date = self.appointment_date,
            time_slot =self.appointment_slot
        )   

    def test_render_calendar_view(self):
        """ Test calendar rendering """
        response = self.client.get(reverse('calendar_view', args=[2024, 8, 19]))
        self.assertEqual(response.status_code, 200)
        # Check the template used for rendering
        self.assertTemplateUsed(response, 'appointment/calendar.html')
        self.assertIn(b'Week of', response.content)
        self.assertIn(b'10:00', response.content)
        self.assertIn(b'17:00', response.content)
        # Check if the service name is in context
        services = response.context['services']
        service_names = [service.name for service in services]
        self.assertIn('General Dentistry', service_names)

    def test_render_calendar_view_with_booked_appointment(self):
        """ Test calendar rendering with previously booked appointment """
        response = self.client.get(reverse('calendar_view', args=[2024, 8, 19]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment/calendar.html')
        # Check the context whether booked slot appears in week_data
        week_data = response.context['week_data']
        appointment_found = False
        for day in week_data:
            if day['date'] == self.appointment_date:
                for slot in day['slots']:
                    if slot['time'] == self.appointment_slot.strftime(
                        '%H:%M') and slot['booked']:
                        appointment_found = True
                        break
        self.assertTrue(
            appointment_found, 
            msg='The booked slot was not found in the calendar'
        )