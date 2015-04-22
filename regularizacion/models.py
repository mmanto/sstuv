from django.db import models
from documentos.models import Expediente
from comun.models import Partido, Departamento


class Censo(models.Model):
    
    expediente= models.ForeignKey(Expediente)
    numero = models.IntegerField()
    fecha = models.DateField('Fecha')
#     tipoEncLegal  
#     expropiación
#     profACargo    
    partido = models.ForeignKey(Partido)
    barrio = models.ForeignKey(Barrio)
