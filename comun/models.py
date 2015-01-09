from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=200)
    #codigo = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Departamento(models.Model):
	nombre = models.CharField(max_length=200)
	# __unicode__ on Python 2
	def __str__(self):
		return self.nombre
