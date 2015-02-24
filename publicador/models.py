from django.db import models
from distutils.command.upload import upload
from tinymce import models as tinymce_models
# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.CharField(max_length=1500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagen_articulo')
    
    def __str__(self):
        return self.titulo