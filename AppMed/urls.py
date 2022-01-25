from django.urls import path
from AppMed import views

urlpatterns = [
    
    path('', views.inicio, name="Inicio"),
    path('quienesSomos/', views.quienesSomos, name="QuienesSomos"),
    path('especialidades/', views.espMedicas, name="Especialidades"),
    path('centros/', views.centroMed, name="Centros"),
    path('profesionales/', views.profesionales, name="Profesionales"),
    path('contacto/', views.contacto, name="Contacto"),
    path('espMedFormulario/', views.espMedFormulario, name="EspMedFormulario"),
    path('centroMedFormulario/', views.centroMedFormulario, name="CentroMedFormulario"),
    path('profFormulario/', views.profFormulario, name="ProfFormulario"),
]
