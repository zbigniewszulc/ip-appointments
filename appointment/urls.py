from django.urls import path
from . import views 

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path('<int:year>/<int:month>/<int:day>/', views.calendar_view, name='calendar_view'),
    path('book/', views.book_appointment, name='book_appointment'),
]