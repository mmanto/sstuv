from django.db import models

class Partido(models.Model):
    
    codigo= models.IntegerField(default=0)
    nombre = models.CharField(max_length=200)
    codcatas = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    
    codigo= models.IntegerField(default=0)
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre