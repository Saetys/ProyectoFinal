from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    
    return HttpResponse('vista inicio')

def espMedicas(request):
    
    return HttpResponse('vista de especialidades médicas')

def centroMed(request):
    
    return HttpResponse('vista de los centros médicos')

def profesionales(request):
    
    return HttpResponse('vista de los profesionales')