from django.db import models

class Partido(models.Model):
    
#     inscripcion = models.CharField(max_length=200)
    codigo= models.IntegerField(default=0)
    
    nombre = models.CharField(max_length=200)
    
    codcas=models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    
#     descripcion = models.CharField(max_length=250)
    codigo= models.IntegerField(default=0)

    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre