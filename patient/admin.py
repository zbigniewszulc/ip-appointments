from django.contrib import admin
from .models import Patient

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'phone_number')
    search_fields = [
        'user', 
        'date_of_birth', 
        'address_line_1', 
        'address_line_2', 
        'address_line_3', 
        'phone_number'
    ]
    list_filter = ('phone_number',)