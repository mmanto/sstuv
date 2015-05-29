from django.db import models
from comun.models import Partido, Departamento
from enum import Enum 
from django.template.defaultfilters import default


class Expediente(models.Model):
	
	organismo = models.IntegerField()
	numero = models.CharField(max_length=200)
	caracteristica = models.CharField(max_length=200)
	fecha_alta = models.DateField('Fecha Alta')
	anio = models.IntegerField()
	alcance = models.CharField(max_length=200)
	cuerpo = models.CharField(max_length=200)
	iniciadopor = models.CharField(max_length=200)
	motivo = models.CharField(max_length=500)
	extracto = models.CharField(max_length=5000)
	cant_fojas= models.IntegerField(default = 0)
	observacion=models.CharField(max_length=10000)
	consolidacion=models.BooleanField(default = False)
	usuarioAlta=models.CharField(max_length=200)

	def __str__(self):
		return self.numero
		
class ExpedienteLey(Expediente):
	
	partido = models.ForeignKey(Partido)
	
	region = models.CharField(max_length=200)
	
	expedientes = models.ForeignKey('self', related_name="expedientes_set")
	
	
	
class Pase(models.Model):
	
	numero = models.IntegerField()
	
	expediente = models.ForeignKey(Expediente, related_name="pase_set")
	
	departamento_origen = models.ForeignKey(Departamento, related_name='origen')
	
	departamento_destino = models.ForeignKey(Departamento, related_name='destino')
	
	fecha = models.DateTimeField('fecha de movimiento')
	
	estado= models.CharField(max_length='50')
	
	def __str__(self):
		return '%s' % self.departamento_origen.nombre
	
	
class Estado(Enum):
	ACEPTADO='Aceptado'
	RECHAZADO='Rechazado'
	PENDIENTE='Pendiente'