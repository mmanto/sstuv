from django.shortcuts import render
from django.db import connections, Error
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist    
from comun import models
from django.http.response import HttpResponse


# Create your views here.
class ImportView():
    
    def importar(self):
        
        mensaje = ''
        
        try:
            cursor = connections['legacy'].cursor()
            ## it's important selecting the id field, so that we can keep the publisher - book relationship
            sql = """SELECT id, codigo, nombre, codcatas FROM partido"""
            cursor.execute(sql)
            for row in cursor.fetchall():
                partidos = models.Partido(id=row[0], codigo=row[1], nombre=row[2], codcatas=row[3])
                partidos.save()
            mensaje = 'Importación realizada con éxito'
        except ConnectionDoesNotExist:
            mensaje = 'legacy database is not configured'
            return None
        except Error:
            mensaje = 'Error.'
        if cursor is None:
            mensaje = 'Cursor None'
        
        return HttpResponse(mensaje)
        
