from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")
register_converter(converters.TwoDigitMonthDayConverter, "md")

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path('<yyyy:year>/<md:month>/<md:day>/', views.calendar_view, name='calendar_view'),
    path('book/', views.book_appointment, name='book_appointment'),
]