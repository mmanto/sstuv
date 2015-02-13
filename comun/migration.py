from django.db import connections, Error
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist    
from comun import models


def setup_cursor():
    try:
        cursor = connections['legacy'].cursor()
        return cursor
    except ConnectionDoesNotExist:
        print("legacy database is not configured")
        return None
    except Error:
        print("Que exception!")


def import_partidos():
    print("import_partidos")    
    cursor = setup_cursor()
    if cursor is None:
        return
    ## it's important selecting the id field, so that we can keep the publisher - book relationship
    sql = """SELECT id, codigo, nombre, codcatas FROM partido"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        partidos = models.Partido(id=row[0], codigo=row[1], nombre=row[2], codcatas=row[3])
        partidos.save()
  

def import_departamentos():
    print("estamos en departamentos")
    cursor = setup_cursor()
    if cursor is None:
        return
    sql = """SELECT id, nombre FROM departamento"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        departamento = models.Departamento(id=row[0], nombre=row[1])
        departamento.save()


def main():
    import_partidos()
    import_departamentos()

main()
#if __name__=="__main__":
    
