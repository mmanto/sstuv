from django.db import connections, Error
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist    
from documentos import models
from comun.models import Partido, Departamento
from documentos.models import Expediente
from datetime import datetime
from asyncio.windows_events import NULL
from tkinter.tix import ROW


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
    sql = """SELECT organismoid, numero, fecha, alcance, cuerpo, añoinicio FROM expediente WHERE not (codlocalidad > 0  and  codregion > 0) """
    cursor.execute(sql)
    for row in cursor.fetchall():
        expediente = models.Expediente(organismo=row[0], numero=row[1], fecha=row[2], alcance=row[3], cuerpo=row[4], anio=row[5])
        expediente.save()
        

def import_expedienteley():
    print("import_expedienteley")    
    cursor = setup_cursor()
    if cursor is None:
        return
  
    sql = """SELECT organismoid, numero, fecha, alcance, cuerpo, codlocalidad, codregion, añoinicio FROM expediente exp WHERE EXISTS(SELECT 1 FROM partido p1 WHERE p1.codigo = exp.codregion) AND EXISTS(SELECT 1 FROM partido p2 WHERE p2.codigo = exp.codlocalidad)"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        partido = Partido.objects.filter(codigo=row[5])
        expedienteley = models.ExpedienteLey(organismo=row[0], numero=row[1], fecha=row[2], alcance=row[3], cuerpo=row[4], partido=partido[0], region=row[6], anio=row[7])
        expedienteley.save()

        
def import_movimientoExpediente():
    print("import_movimientoExpediente")    
    cursor = setup_cursor()
    if cursor is None:
        return
  
    sql = """SELECT mov.connro, exp.organismoid, exp.numero, exp.añoinicio FROM movimiento mov INNER JOIN expediente exp ON mov.clavereg = exp.claveregion"""
#     sql2 = """SELECT mov.connro, exp.organismoid, exp.numero, exp.añoinicio FROM movimiento mov LEFT JOIN expediente exp ON mov.clavereg = exp.claveregion where exp.organismoid = 2423 and exp.numero = 242 and exp.añoinicio = 2012"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        print('organismo str: ' + str(row[1]))
        print('numero: ' + str(row[2]))
        print('anio: ' + str(row[3]))    
        expediente = Expediente.objects.filter(organismo=str(row[1]), numero=str(row[2]), anio=row[3] )
        print( expediente )
        print( 'organismo: ' + expediente[0].organismo )
        print( 'numero: ' + expediente[0].numero )
        print( 'anio: ' + str(expediente[0].anio) )
        if len(expediente) > 0:
            print(row)
            print("expediente: ")
            print(expediente)
            print('departameneto ' + str(row[0]))
            departamento = Departamento.objects.filter(codigo=row[0])
            print(departamento)
            if len(departamento) > 0:
                print('dentro')
                pase = models.Pase()
                pase.expediente=expediente[0]
                pase.departamento_origen=departamento[0]
                pase.departamento_destino=departamento[0]
                pase.fecha=datetime.now()
                pase.save()

def main():
    import_expediente()
    import_expedienteley()
    import_movimientoExpediente()


main()
# if __name__=="__main__":
    
