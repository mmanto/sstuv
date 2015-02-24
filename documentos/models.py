from django.db import models
from comun.models import Partido, Departamento

class Expediente(models.Model):
	
	organismo = models.IntegerField()
	numero = models.CharField(max_length=200)
	anio = models.IntegerField()
	
	caracteristica = models.CharField(max_length=200)
	fecha = models.DateField('Fecha')
	alcance = models.CharField(max_length=200)
	cuerpo = models.CharField(max_length=200)
	
	def __str__(self):
		return self.numero
		
class ExpedienteLey(Expediente):
	
	partido = models.ForeignKey(Partido)
	
	region = models.CharField(max_length=200)
	
	
class Pase(models.Model):
	
	expediente = models.ForeignKey(Expediente, related_name="pase_set")
	
	departamento_origen = models.ForeignKey(Departamento, related_name='origen')
	
	departamento_destino = models.ForeignKey(Departamento, related_name='destino')
	
	fecha = models.DateTimeField('fecha de movimiento')
	
	def __str__(self):
		return '%s' % self.departamento_origen.nombre