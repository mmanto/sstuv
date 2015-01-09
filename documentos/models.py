from django.db import models
from comun.models import Partido, Departamento

class Expediente(models.Model):
	caracteristica = models.CharField(max_length=200)
# numero = models.IntegerField(default=0)
	numero = models.CharField(max_length=200)
	fecha = models.DateField('Fecha')
	alcance = models.CharField(max_length=200)
	cuerpo = models.CharField(max_length=200)
		
	def __str__(self):
		return self.numero
		
class ExpedienteLey(Expediente):
	#expediente = models.ForeignKey(Expediente)
    #partido = models.ForeignKey(Partido)
    partido = models.OneToOneField(Partido)
    region = models.CharField(max_length=200)
	
class Pase(models.Model):
	expediente = models.ForeignKey(Expediente)
	departamento_origen = models.OneToOneField(Departamento, primary_key=True)
	fecha = models.DateTimeField('fecha de movimiento')
	def __str__(self):
		return '%s' % self.departamento_origen.nombre

