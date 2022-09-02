from django.urls import path
from AppCoder import views
from .views import *



urlpatterns = [
   
    
    path('curso', views.curso, name="curso"),
    path('Estudiantes/', views.Estudiantes, name='Estudiantes'),
    path("Profesores/", views.Profesores, name='Profesores'),
    path('', views.inicio),
    path('cursoFormulario/',cursoFormulario, name= 'cursoFormulario'),
    path('estudiantesFormulario/',estudiantesFormulario, name= 'estudiantesFormulario'),
    path('profesoresFormulario/',profesoresFormulario, name= 'profesoresFormulario'),
    path('busquedaCamada', views.busquedaCamada, name='busquedaCamada'),
    path('buscar/', views.buscar),
]