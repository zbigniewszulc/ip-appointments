from django.urls import path
from patient import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),
    path('cancel_appointment/<int:appointment_id>/', views.cancel_appointment, 
         name='cancel_appointment'),
    path('my_details/', views.my_details, name='my_details'),
    path('my_details/edit', views.edit_my_details, name='edit_my_details'),
]
