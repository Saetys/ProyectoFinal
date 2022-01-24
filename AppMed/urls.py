from django.urls import path
from AppMed import views

urlpatterns = [
    
    path('', views.inicio),
    path('especialidadesMedicas/', views.espMedicas, name="EspecialidadesMedicas"),
    path('centrosMedicos/', views.centroMed, name="CentrosMedicos"),
    path('profesionales/', views.profesionales, name="Profesionales"),
]
