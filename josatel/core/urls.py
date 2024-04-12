from django.urls import path
from . import views


urlpatterns = [
    # Ventanas principales
    path('', views.index, name='index'),
    path('servicios/', views.servicios, name='servicios'),
    path('experienciayclientes/', views.experienciayclientes, name='experienciayclientes'),
    path('contacto/', views.contacto, name='contacto'),
]