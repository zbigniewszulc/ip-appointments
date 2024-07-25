from django.contrib import admin
from .models import Service, Appointment

# Register your models here.
admin.site.register(Service)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'service', 'date', 'time_slot')
    search_fields = ['patient', 'service']
    list_filter = ('date', 'service',)