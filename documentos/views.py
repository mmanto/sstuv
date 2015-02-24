from django.shortcuts import render
from django.views.generic import ListView
from documentos.models import ExpedienteLey, Expediente, Pase
from django.core.context_processors import request
from documentos.forms import ExpedienteLeyForm, ExpedienteForm, PaseForm
from comun.models import Partido, Departamento
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.http import HttpResponseRedirect
from django.template import RequestContext 
from idlelib.SearchEngine import get
from asyncio.base_events import Server
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connections, Error
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist
from django.http.response import HttpResponse
from documentos import models    
from datetime import datetime
from django.conf.global_settings import DATE_FORMAT   
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger('sstuv') 


class LoginView(ListView):
    
    
    def login(request, template_name='registration/login.html'):
       
        return render(request, 'login.html')
        
    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def home(request, template_name='registration/login.html'):
        return HttpResponseRedirect('/sig/expedientes/')
                    
    def logout(request):
        template_name = 'auth/login_out.html'
        return logout_then_login(request,login_url='/sig/auth/login')
        
    def get_queryset(self):
        return ExpedienteLey.objects.all()
    
    
class ExpedientesView(ListView):
    paginate_by = 10
    
#     def __init__(self):
#         self.logger = logging.getLogger('documentos.views.ExpedientesView')
        
    
    def showExpediente(request, tipo, organismo, numero, anio):
    
        organismo=int(organismo)
        numero= int(numero)
        anio=int(anio)
            
        partidos =  Partido.objects.all()
       
        departamentos=Departamento.objects.all()
        
        if(numero != 0):  #Expediente editar
            
            if(tipo == 'ExpedienteLey'):
                expediente = ExpedienteLey.objects.get(organismo=organismo, numero=numero, anio=anio)
            else:
                expediente = Expediente.objects.get(organismo=organismo, numero=numero, anio=anio)

#             pases = expediente.pase_set.all()
        
            pases = ExpedientesView.paginador(request, expediente.pase_set.all())



            return render(request, 'expediente_ley.html', {'expediente': expediente, 'partidos': partidos, 'departamentos':departamentos, 'tipo':tipo, 'accion':'editar', 'pases':pases, 'organismoFiltro' : organismo, 'numeroFiltro': numero, 'anioFiltro' :anio}, context_instance=RequestContext(request) )
      
        else: # Expediente nuevo
            return render(request, 'expediente_ley.html', {'partidos': partidos, 'departamentos':departamentos, 'tipo':tipo, 'accion':'nuevo'},context_instance=RequestContext(request))
        
    
 
    def loadBusquedaExpediente(request):
        logger.info('busqueda de expedientes en logger info')
        logger.error('busqueda de expedientes en logger error')
        return render(request, 'expedienteley_list.html', {'tipo' : 'Expediente'}, context_instance=RequestContext(request))
    

    def loadBusquedaExpedienteLey(request):
        return render(request, 'expedienteley_list.html', {'tipo' : 'ExpedienteLey'}, context_instance=RequestContext(request))

    def showResultados(request, tipo):
        
        
        expedientes= []
        
        organismo=int(request.GET['organismo'])
        numero=int(request.GET['numero'])
        anio=int(request.GET['anio'])
        
        if numero == 0  :
                expedientes = Expediente.objects.all()
        else :
             
                try:
                    if(tipo == 'ExpedienteLey'):
                       if(ExpedienteLey.objects.filter(organismo=organismo, numero=numero, anio=anio ).exists()):         
                            expedientes.append(ExpedienteLey.objects.get(organismo=organismo, numero=numero, anio=anio))
                    else:    
                         if(Expediente.objects.filter(organismo=organismo, numero=numero, anio=anio).exists()):         
                            expedientes.append(Expediente.objects.get(organismo=organismo, numero=numero, anio=anio))
                except:         
                    expedientes= []
         
        paginator = Paginator(expedientes, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            expedientes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            expedientes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            expedientes = paginator.page(paginator.num_pages)           
        
        return render_to_response('expedienteley_list.html', {'expedientes' : expedientes, 'tipo' : tipo, 'organismoFiltro' : organismo, 'numeroFiltro': numero, 'anioFiltro' :anio }, context_instance=RequestContext(request))
    
    def saveExpediente(request):
        
        valido=False
        tipo= request.POST.get('tipo','')
        
        if request.method == 'POST':
       
            if(tipo == 'Expediente'):
                form = ExpedienteForm(request.POST)
            else:
                form = ExpedienteLeyForm(request.POST)
                form.model.partido = Departamento.objects.get( codigo = int (request.POST.get('partido')))
    
            errores=[]    
            if form.is_valid():
               
                #Validación para que no se repita el número de expediente. TODO: refactor
                if(Expediente.objects.filter(organismo = request.POST.get('organismo') ,numero = request.POST.get('numero'), anio =  request.POST.get('anio')).exists()):
                    errores.append('El número de expediente ya existe.')
                else:
                    form.save()
                    valido=True   
        
        if(valido): #Exito       
            return render(request, 'expedienteley_list.html',{'tipo' : tipo}, context_instance=RequestContext(request))
        else:  # Error
            
            errores.append(form._errors)
            
            expediente =Expediente()
            expediente.organismo=request.POST.get('organismo')
            expediente.numero = request.POST.get('numero')
            expediente.anio =request.POST.get('anio')
            expediente.caracteristica=request.POST.get('caracteristica')
            expediente.fecha = datetime.strptime( request.POST.get('fecha'), "%m/%d/%Y")   #datetime.strptime( fecha, "%M/%d/%Y" )
            expediente.alcance=request.POST.get('alcance')
            expediente.cuerpo=request.POST.get('cuerpo')
                  
            return render(request, 'expediente_ley.html', {'tipo' : tipo,'expediente': expediente ,'form':form ,'accion' : 'nuevo', "errores":errores}, context_instance=RequestContext(request) )


    def updateExpediente(request):
    
            tipo= request.POST.get('tipo','')
            numero = request.POST.get('numero','')
            
        
            if request.method == 'POST':
                form=''
                if(tipo == 'Expediente'):
                    
                    expediente = Expediente.objects.get(numero = numero)
                    
                    form = ExpedienteForm(request.POST, instance=expediente)
                else:
                    form = ExpedienteLeyForm(request.POST)
                    
                if form.is_valid():  
                     form.save()   
                else:
                    return render(request, 'expediente_ley.html',{'tipo' : tipo, 'expediente': expediente, 'form':form, 'accion' : 'editar'})
            
            return render(request, 'expedienteley_list.html',{'tipo' : tipo})
        
    def importarExpedientesLey(self):
        sql = """SELECT id, partido_id, alcance, cuerpo, extracto, fecha_inicio, tipo_expediente, tipo_expediente_id, barrio_id, numero, fechas FROM expediente where cuerpo <> '' """
        mensaje = ''
    
        try:
            cursor = connections['legacy'].cursor()
            ## it's important selecting the id field, so that we can keep the publisher - book relationship
            #sql = """SELECT id, codigo, nombre, codcatas FROM partido"""
            cursor.execute(sql)
            for row in cursor.fetchall():
                expedientesLey = models.ExpedienteLey(id=row[0], partido_id=row[1], alcance=row[2], cuerpo=row[3], extracto=row[4], fecha_inicio=row[5], tipo_expediente=row[6], barrio_id=row[7], numero=row[8], fechas=row[9])
                expedientesLey.save()
            mensaje = 'Importación realizada con éxito'
        except ConnectionDoesNotExist:
            mensaje = 'legacy database is not configured'
            return None
        except Error:
            mensaje = 'Error.'
        if cursor is None:
            mensaje = 'Cursor None'
        
        return HttpResponse(mensaje)
        
    def importarExpedientes(self):

        mensaje = ''
    
        try:
            cursor = connections['legacy'].cursor()
            ## it's important selecting the id field, so that we can keep the publisher - book relationship
            #sql = """SELECT id, codigo, nombre, codcatas FROM partido"""
            #extracto,  tipo_expediente, tipo_expediente_id, barrio_id, fechas
            cursor.execute("""SELECT id, numero, fecha_inicio, cuerpo FROM expediente where cuerpo = '' """)
            for row in cursor.fetchall():
                #caracteristica=row[1]
                #alcance=row[4],
                partidos = models.Expediente(id=row[0], numero=row[1], fecha=row[2], cuerpo=row[3])
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
  
    def get_queryset(self):
        return ExpedienteLey.objects.all()


    def paginador(request, object):
        paginator = Paginator(object, 5) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            object = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            object = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            object = paginator.page(paginator.num_pages)   
        return object



class PasesView(ListView):
    
    
    #Se persiste un Pase    
    def savePase(request):
                 
        pase = Pase()
           
        pase.departamento_origen = Departamento.objects.get( codigo = int (request.POST.get('departamento_origen')))
         
        pase.departamento_destino = Departamento.objects.get( codigo = int (request.POST.get('departamento_destino')))
               
        fecha= (request.POST.get('fecha'))
                       
        pase.fecha =  datetime.strptime( fecha, "%m/%d/%Y" )

        pase.expediente = Expediente.objects.get( id = int (request.POST.get('expediente_id')))
      
        pase.save()
      
        return ExpedientesView.showExpediente(request, request.POST.get('expediente_tipo'), pase.expediente.organismo, pase.expediente.numero, pase.expediente.anio)

            
         #TODO   
    def removePase(request):

        return ExpedientesView.showExpediente(request, request.POST.get('Expediente'), request.POST.get('expediente_id'))

            
            
            
            
            
            
    
