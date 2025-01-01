from django.urls import path
from patient import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),
]