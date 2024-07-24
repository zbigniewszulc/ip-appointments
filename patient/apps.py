# Import base class for configuration
from django.apps import AppConfig

class PatientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patient'
    # ready() - special method provided by 'AppConfig'
    def ready(self):
        # Register signal handlers when application starts
        import patient.signals