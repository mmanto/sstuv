from django.db import connections, Error
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist    
from comun import models

def setup_cursor():
    try:
        cursor = connections['legacy'].cursor()
    except ConnectionDoesNotExist:
        print("legacy database is not configured")
        return None
    except Error:
        print("Que exception!")

def import_partidos():
    cursor = setup_cursor()
    if cursor is None:
        return
    ## it's important selecting the id field, so that we can keep the publisher - book relationship
    sql = """SELECT id, codigo, nombre, codcas FROM partido"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        partidos = models.Partido(id=row[0], codigo=row[1], nombre=row[2], codcas=row[3])
        partidos.save()

def main():
    import_partidos()
    

if __name__=="__main__":
    main()
