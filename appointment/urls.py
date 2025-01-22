from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")
register_converter(converters.TwoDigitMonthDayConverter, "md")

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path(
        '<yyyy:year>/<md:month>/<md:day>/',
        views.calendar_view,
        name='calendar_view'
    ),
    path('book/', views.book_appointment, name='book_appointment'),
    path('services/', views.get_services, name='get_services'),
    path('services/add/', views.add_service, name='add_service'),
    path(
        'services/edit/<int:service_id>/',
        views.edit_service,
        name='edit_service'
    ),
    path(
        'services/delete/<int:service_id>/',
        views.delete_service, name='delete_service'
    ),
]
