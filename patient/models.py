from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="patient"
    )
    date_of_birth = models.DateField()
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    address_line3 = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15)

    class Meta: 
        # refer to a field of related model 'User' by using '__'
        # '__' - used to navigate throught related models
        ordering = ["user__last_name", "user__first_name"]

    def __str__(self):
        return f"Name: {self.user.first_name}  {self.user.last_name} - - - \
            Email: {self.user.email} - - - \
            Phone: {self.phone_number}"