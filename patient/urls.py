from django.urls import path
from patient import views 

urlpatterns = [
    path('', views.index, name='index'),
]