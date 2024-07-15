from django.urls import path
from hello_world import views as index_views

urlpatterns = [
    path('', index_views.index, name='index'),
]