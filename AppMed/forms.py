from django import forms

class EspMedFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    codigo=forms.IntegerField()
    
class CentroMedFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    direccion=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
    email=forms.EmailField()
    web=forms.CharField(max_length=40)
    
class ProfFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    especialidad=forms.CharField(max_length=30)
    atencion=forms.CharField(max_length=30)
    
