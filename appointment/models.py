from django.db import models
from patient.models import Patient

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=50) 
    
    def __str__(self):
	    return self.name
        
class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        related_name='appointment'
    )
    service = models.ForeignKey(
        Service, 
        on_delete=models.CASCADE,
        related_name='service_type'
    )
    date = models.DateField()
    time_slot = models.TimeField()
    booked_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self): 
	    return f'{self.patient.user.username} - ' \
            f'{self.service.name} - {self.date} {self.time_slot}'