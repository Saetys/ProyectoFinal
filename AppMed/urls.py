from django.urls import path
from AppMed import views

urlpatterns = [
    
    path('', views.inicio),
    path('sobreNosotros/', views.sobreNos, name="SobreNosotros"),
    path('especialidades/', views.espMedicas, name="Especialidades"),
    path('centros/', views.centroMed, name="Centros"),
    path('profesionales/', views.profesionales, name="Profesionales"),
    path('contacto/', views.contacto, name="Contacto"),
]
