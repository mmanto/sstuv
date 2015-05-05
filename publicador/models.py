from django.db import models
from distutils.command.upload import upload
# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=500)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Imagen(models.Model):
    imagen = models.ImageField(upload_to='imagen_articulo')
    articulo = models.ForeignKey(Articulo, related_name = 'imagenes')

    def __str__(self):
        return str(self.imagen)

