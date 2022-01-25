from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    
    return render (request, "AppMed/inicio.html")

def quienesSomos(request):
    
    return render (request, "AppMed/quienesSomos.html")

def espMedicas(request):
    
    return render (request, "AppMed/espMedicas.html")

def centroMed(request):
    
    return render (request, "AppMed/centroMed.html")

def profesionales(request):
    
    return render (request, "AppMed/profesionales.html")

def contacto(request):
    
    return render (request, "AppMed/contacto.html")   