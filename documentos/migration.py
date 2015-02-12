from django.db import connections, Error
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist    
from documentos import models
from comun.models import Partido


def setup_cursor():
    try:
        cursor = connections['legacy'].cursor()
        return cursor
    except ConnectionDoesNotExist:
        print("legacy database is not configured")
        return None
    except Error:
        print("Que exception!")


def import_expediente():
    print("import_expediente")    
    cursor = setup_cursor()
    if cursor is None:
        return
    ## it's important selecting the id field, so that we can keep the publisher - book relationship
    sql = """SELECT organismoid, numero, fecha, alcance, cuerpo FROM expediente WHERE codlocalidad = 0 and codregion = 0"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        expediente = models.Expediente(caracteristica=row[0], numero=row[1], fecha=row[2], alcance=row[3], cuerpo=row[4])
        expediente.save()
        

def import_expedienteley():
    print("import_expedienteley")    
    cursor = setup_cursor()
    if cursor is None:
        return
  
    sql = """SELECT organismoid, numero, fecha, alcance, cuerpo, codlocalidad, codregion FROM expediente exp WHERE EXISTS(SELECT 1 FROM partido p1 WHERE p1.codigo = exp.codregion) AND EXISTS(SELECT 1 FROM partido p2 WHERE p2.codigo = exp.codlocalidad)"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        partido = Partido.objects.filter(codigo=row[5])
        expedienteley = models.ExpedienteLey(caracteristica=row[0], numero=row[1], fecha=row[2], alcance=row[3], cuerpo=row[4], partido=partido[0], region=row[6])
        expedienteley.save()

  
def main():
    import_expediente()
    import_expedienteley()


main()
# if __name__=="__main__":
    
