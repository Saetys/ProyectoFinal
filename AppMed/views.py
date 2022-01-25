from django.shortcuts import render
from django.http import HttpResponse
from AppMed.models import EspMedicas, CentroMed, Profesional
from AppMed.forms import EspMedFormulario, CentroMedFormulario, ProfFormulario

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

def espMedFormulario(request):
    
    if(request.method == 'POST'):
        
        mi_formulario= EspMedFormulario(request.POST)
        
        if(mi_formulario.is_valid()):
            
            data= mi_formulario.cleaned_data
                  
            espMedicas= EspMedicas(nombre=data['nombre'], codigo=data['codigo'])
        
            espMedicas.save()
    
            return render(request, "AppMed/inicio.html")
        
        else:
            
            return HttpResponse('FORMULARIO NO VALIDO')
        
    else:
        
        mi_formulario= EspMedFormulario()
                
    return render(request, "AppMed/espMedFormulario.html", {'form': mi_formulario})


def centroMedFormulario(request):
    
    if(request.method == 'POST'):
        
        mi_formulario= CentroMedFormulario(request.POST)
        
        if(mi_formulario.is_valid()):
            
            data= mi_formulario.cleaned_data
                  
            centroMed= CentroMed(nombre=data['nombre'], direccion=data['direccion'], 
             telefono=data['telefono'], email=data['email'], web=data['web'])
        
            centroMed.save()
    
            return render(request, "AppMed/inicio.html")
        
        else:
            
            return HttpResponse('FORMULARIO NO VALIDO')
        
    else:
        
        mi_formulario= CentroMedFormulario()
                
    return render(request, "AppMed/centroMedFormulario.html", {'form': mi_formulario})


def profFormulario(request):
    
    if(request.method == 'POST'):
        
        mi_formulario= ProfFormulario(request.POST)
        
        if(mi_formulario.is_valid()):
            
            data= mi_formulario.cleaned_data
                  
            profesional= Profesional(nombre=data['nombre'], apellido=data['apellido'], 
             especialidad=data['especialidad'], atencion=data['atencion'])
        
            profesional.save()
    
            return render(request, "AppMed/inicio.html")
        
        else:
            
            return HttpResponse('FORMULARIO NO VALIDO')
        
    else:
        
        mi_formulario= ProfFormulario()
                
    return render(request, "AppMed/profFormulario.html", {'form': mi_formulario})
   