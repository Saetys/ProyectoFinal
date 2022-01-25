from django.db import models

class EspMedicas(models.Model):
    
    nombre=models.CharField(max_length=40)
    codigo=models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - {self.codigo}'


class CentroMed(models.Model):
    
    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()
    web=models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.nombre}'
    

class Profesional(models.Model):
    
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    especialidad=models.CharField(max_length=30)
    atencion=models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre} - {self.especialidad}'
