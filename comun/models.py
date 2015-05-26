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
    
#     
# class Partido():
#     nomencla= models.CharField()
#     nombre=models.CharField
#     cod_depto=models.CharField   
# class PartidoDTO(models.Model):
#     objectId:89,
#         "DEPARTA":"ALMIRANTE BROWN",
#         "CABECER":"ADROGUE",
#         "PROVINCIA":"BUENOS AIRES",
#         "FUENTE":"CATASTRO BUENOS AIRES",
#         "FEC_ACTUAL":"MAR 2006",
#         "FUENTE1":"CATASTROS PROVINCIALES",
#         "COD_DEPTO":"06028",
#         "NOMBRE":"Almirante Brown",
#         "NOMENCLA":"003"