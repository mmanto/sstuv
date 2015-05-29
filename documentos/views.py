from django.shortcuts import render
from django.views.generic import ListView
from documentos.models import ExpedienteLey, Expediente, Pase, Estado
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
import datetime
from django.conf.global_settings import DATE_FORMAT   
import logging
logger = logging.getLogger('sstuvInfo')
loggerError = logging.getLogger('sstuvError')
from django.db.models import Q 
from django.db import connection
from datetime import date
from django.core import serializers




class ExpedientesView(ListView):
        
    paginate_by = 10
    search_fields = ('organismo', 'numero', 'anio')
    
    '''
    Controller: carga un expediente ya se para la carga o para visualizarlo.   
    '''
    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def showExpediente(request, id):

        departamentosInternos = Departamento.objects.filter(codigo__gt=999, codigo__lt=6001).order_by("nombre")
        departamentosExternos = Departamento.objects.filter(codigo__gt=13, codigo__lt=72).all().order_by("nombre")
        partidos = Partido.objects.all()

        if(id != '0'):  #Expediente editar
             
            if ( ExpedienteLey.objects.filter(id = id).exists()):
                expediente= ExpedienteLey.objects.get(id=id)
            else: 
                expediente= Expediente.objects.get(id=id)
       
            pases = ExpedientesView.paginador(request, expediente.pase_set.all())
            if len(pases) > 0:
                pase_id_actual = expediente.pase_set.last().id
                print (pase_id_actual)
            else:
                pase_id_actual = 0                                
<<<<<<< HEAD
    
=======

>>>>>>> origin/vdiaz
            pase_id_actual = pase_id_actual + 1
            proximo_pase_id = pase_id_actual  
            proximo_pase_id = str(proximo_pase_id) + str(datetime.date.today().year)

            return render(request, 'expediente_ley.html', {'expediente': expediente , 'pases':pases ,  'partidos': partidos, 'departamentosInternos':departamentosInternos, 'departamentosExternos':departamentosExternos, 'proximo_pase_id':  proximo_pase_id }, context_instance=RequestContext(request))
       
        else:  # Expediente nuevo
            return render(request, 'expediente_ley.html', {'partidos': partidos, 'departamentosInternos':departamentosInternos, 'departamentosExternos':departamentosExternos}, context_instance=RequestContext(request))
      
    '''
     Controller: redirect al template para la carga de expediente 
    ''' 
    def nuevoExpediente (request):
        departamentosInternos = Departamento.objects.filter(codigo__gt=999, codigo__lt=6001).order_by("nombre")
        departamentosExternos = Departamento.objects.filter(codigo__gt=13, codigo__lt=72).all().order_by("nombre")
        partidos = Partido.objects.all()
        
        return render(request, 'expediente_ley.html', {'partidos': partidos, 'departamentosInternos':departamentosInternos, 'departamentosExternos':departamentosExternos, 'tipo':'Expediente'}, context_instance=RequestContext(request))

    
    
    '''
     Controller: redirect al template para la carga de expedienteLey 
     '''  
    def nuevoExpedienteLey (request):
        departamentosInternos = Departamento.objects.filter(codigo__gt=999, codigo__lt=6001).order_by("nombre")
        departamentosExternos = Departamento.objects.filter(codigo__gt=13, codigo__lt=72).all().order_by("nombre")
        partidos = Partido.objects.all()
        
        return render(request, 'expediente_ley.html', {'partidos': partidos, 'departamentosInternos':departamentosInternos, 'departamentosExternos':departamentosExternos, 'tipo':'ExpedienteLey'}, context_instance=RequestContext(request))

        
    
    '''
     Controller: Se carga la búsqueda
    '''
    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def loadBusquedaExpediente(request):
        logger.info('busqueda de expedientes en logger info')
        loggerError.error('busqueda de expedientes en logger error')
        return render(request, 'expedienteley_list.html', {'tipo' : 'Expediente'}, context_instance=RequestContext(request))
    
    '''
    Controller: 
    '''
    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def loadBusquedaExpedienteLey(request):
        return render(request, 'expedienteley_list.html', {'tipo' : 'ExpedienteLey'}, context_instance=RequestContext(request))

    '''
    Controller : Búsqueda de expedientes.
    
    '''
    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def showResultados(request):
        
        expedientes = []
        expedientesLey = []
        filter_dict = {}
        page = request.GET.get('page')
        print (page)
        
        if( page != None  ):
            filter_dict=request.session['filtroExpediente']
        else:    
           
            # Se crea el filtro
            organismo = ExpedientesView.toInt(request.GET['organismo'])
            numero = ExpedientesView.toInt(request.GET['numero'])
            anio = ExpedientesView.toInt(request.GET['anio'])
            buscarExpPropios=(request.GET['radio'])
            filter_dict['alcance'] = alcance = ExpedientesView.toInt(request.GET['alcance'])
            extracto= request.GET['extracto']
            
            if (organismo > 0):     filter_dict['organismo'] = organismo
            if (numero > 0):        filter_dict['numero'] = numero
            if (anio > 0):          filter_dict['anio'] = anio
#             if((tipo == 'ExpedienteLey')): 
#                 consolidacion = bool(request.GET['consolidacion'])
#                 filter_dict['consolidacion'] = consolidacion
            if(buscarExpPropios == 'propio'):
                filter_dict['pase_set__departamento_destino__nombre'] = request.user.groups.all().first().name    
                filter_dict['pase_set__estado']= Estado.ACEPTADO.value   
            if(extracto != ''):
                filter_dict['extracto__icontains'] = extracto
            
            
            request.session['filtroExpediente']= filter_dict  
<<<<<<< HEAD
            
     
        expedientes = (list( Expediente.objects.filter(**filter_dict).distinct() ))
        expedientesLey = (list( ExpedienteLey.objects.filter(**filter_dict).distinct() ))
            
            
        expedientes.extend(expedientesLey)
      
        paginator = Paginator(expedientes, 10) 
=======
                     
        if(len(filter_dict) > 0):
            if (tipo == 'Expediente'):
                expedientes = ( Expediente.objects.filter(**filter_dict).distinct() )
            elif (tipo == 'ExpedienteLey'):
                expedientes = ( ExpedienteLey.objects.filter(**filter_dict).distinct() )
                
        paginator = Paginator(expedientes, 10)  # Show 25 contacts per page
>>>>>>> origin/vdiaz

        try:
            expedientes = paginator.page(page)
        except PageNotAnInteger:
            expedientes = paginator.page(1)
        except EmptyPage:
            expedientes = paginator.page(paginator.num_pages)           
        

        return render_to_response('expedienteley_list.html', {'expedientes' : expedientes, }, context_instance=RequestContext(request))
    
    '''   
    Controller : Persiste el expediente
      
    ''' 
    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def saveExpediente(request):
    
        continueIn = request.POST.get('continueIn', '')
        saveData = request.POST.get('saveData', '')
        valido = False
        tipo = request.POST.get('tipo', '')
        departamentosInternos = Departamento.objects.filter(codigo__gt=999, codigo__lt=6001).order_by("nombre")
        departamentosExternos = Departamento.objects.filter(codigo__gt=13, codigo__lt=72).all().order_by("nombre")

        if (request.method == 'POST'):
            
            if(tipo == 'Expediente'):        form = ExpedienteForm(request.POST)
            else:     form = ExpedienteLeyForm(request.POST)
   
            errores = []    

            if (continueIn == 'save-continue' or continueIn == 'save-exit'):                
                if form.is_valid():
                    
                    # Validación para que no se repita el número de expediente. 
                    if(Expediente.objects.filter(organismo=request.POST.get('organismo') , numero=request.POST.get('numero'), anio=request.POST.get('anio')).exists()):
                        errores.append('El número de expediente ya existe.')
                    
                    else:  # Persiste Expediente y agrega auditoria                        
                        exp =  form.save()
                        exp.usuarioAlta=request.user.username
                        exp =  form.save()
                        depto_origen = Departamento.objects.get( codigo = 1150 )
                        depto_destino = Departamento.objects.get( codigo = 1150 )
                        guardar_pase( depto_origen, depto_destino, exp )
                        valido = True 
                        
                        if(continueIn == "save-continue"): #Redirección al templete de expediente para seguir cargando
                            return render(request, 'expediente_ley.html', {'tipo' : tipo, 'form':form , 'accion' : 'nuevo', 'departamentosInternos':departamentosInternos, 'departamentosExternos':departamentosExternos , "errores":errores}, context_instance=RequestContext(request))

                        if(continueIn == "save-exit"): #Redirección al tempalte de expedeinte_list   
                            return render(request, 'expedienteley_list.html', {'tipo' : tipo}, context_instance=RequestContext(request))
                
                
                if(not valido): #Error  en la validación del formulario
                    
                    errores.append(form._errors)
                    expediente = Expediente()
                    expediente.organismo = request.POST.get('organismo')
                    expediente.numero = request.POST.get('numero')
                    expediente.fecha_alta = request.POST.get('fecha_alta')
                    expediente.caracteristica = request.POST.get('caracteristica')
                    print(request.POST.get('anio'))
                    expediente.anio = datetime.datetime.strptime(request.POST.get('anio'), "%Y")  # datetime.strptime( fecha, "%M/%d/%Y" )
                    expediente.alcance = request.POST.get('alcance')
                    expediente.cuerpo = request.POST.get('cuerpo')
                    print("entro por el else invalido")
               
                    
                    return render(request, 'expediente_ley.html', {'tipo' : tipo, 'expediente': expediente , 'form':form , 'accion' : 'nuevo', 'departamentosInternos':departamentosInternos, 'departamentosExternos':departamentosExternos , "errores":errores}, context_instance=RequestContext(request))
                
            if (continueIn == 'exit'): #Exit: Redirección al template expediente_list
                return render(request, 'expedienteley_list.html', {'tipo' : tipo}, context_instance=RequestContext(request))

        return render(request, 'expedienteley_list.html', {'tipo' : tipo}, context_instance=RequestContext(request))    
            
            
            
            
            
           
    '''    
    Controller:   Upadate de expediente
    '''            
    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def updateExpediente(request):
    
        tipo = request.POST.get('tipo', '')
        organismo = int(request.POST.get('organismo'))
        numero = int(request.POST.get('numero'))
        anio = int(request.POST.get('anio'))
        
        if request.method == 'POST':
                form = ''
                if(tipo == 'Expediente'):
                    expediente = Expediente.objects.get(organismo=organismo, numero=numero, anio=anio)
                    form = ExpedienteForm(request.POST, instance=expediente)
                else:
                    expediente = ExpedienteLey.objects.get(organismo=organismo, numero=numero, anio=anio)
                    form = ExpedienteLeyForm(request.POST, instance=expediente)
                    
                if form.is_valid():  
                     form.save()   
                else:
                    return render(request, 'expediente_ley.html', {'tipo' : tipo, 'expediente': expediente, 'form':form, 'accion' : 'editar'})
            
        return render(request, 'expedienteley_list.html', {'tipo' : tipo})

    #Exit of the expediente
    # 
    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def exitExpediente(request):
        tipo = request.POST.get('exp_tipo', '')
        return render(request, 'expedienteley_list.html', {'tipo' : tipo}, context_instance=RequestContext(request))

    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def importarExpedientesLey(self):
        sql = """SELECT id, partido_id, alcance, cuerpo, extracto, anio, tipo_expediente, tipo_expediente_id, barrio_id, numero, fechas FROM expediente where cuerpo <> '' """
        mensaje = ''
    
        try:
            cursor = connections['legacy'].cursor()
            # # it's important selecting the id field, so that we can keep the publisher - book relationship
            # sql = """SELECT id, codigo, nombre, codcatas FROM partido"""
            cursor.execute(sql)
            for row in cursor.fetchall():
                expedientesLey = models.ExpedienteLey(id=row[0], partido_id=row[1], alcance=row[2], cuerpo=row[3], extracto=row[4], anio=row[5], tipo_expediente=row[6], barrio_id=row[7], numero=row[8], fechas=row[9])
                expedientesLey.save()
            mensaje = 'Importación realizada con éxito'
        except ConnectionDoesNotExist:
            logger.error("BD Caida")
            mensaje = 'Base de datos fuera de linea.'
            return None
        except Error:
            logger.error("Error inestperado al importar expedientes Ley")
            mensaje = 'Sistema en mantenimiento, intentelo en unos momentos.'
        if cursor is None:
            mensaje = 'Cursor None'
        
        return HttpResponse(mensaje)
        
    def importarExpedientes(self):

        mensaje = ''
    
        try:
            cursor = connections['legacy'].cursor()
            # # it's important selecting the id field, so that we can keep the publisher - book relationship
            # sql = """SELECT id, codigo, nombre, codcatas FROM partido"""
            # extracto,  tipo_expediente, tipo_expediente_id, barrio_id, fechas
            cursor.execute("""SELECT id, numero, anio, cuerpo FROM expediente where cuerpo = '' """)
            for row in cursor.fetchall():
                # caracteristica=row[1]
                # alcance=row[4],
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
        paginator = Paginator(object, 5)  # Show 25 contacts per page
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

    #  
#   Utilitario para castear de forma segura valores numericos  
#  
    def toInt(valor):
        
        try: 
            x = int(valor)
        except ValueError:
            x = 0
        return x    
 



class PasesView(ListView):
    
    
    def getPases(request):
        
        pases = []
        user = request.user
        try :
            departamento = Departamento.objects.get(nombre=user.groups.first())
            
            pases = PasesView.paginador(request, Pase.objects.filter(estado=Estado.PENDIENTE.value , departamento_destino=departamento).all())
        except Error:
            logger.info('Error al recuperar los pases con el usuuario' + user)    

        
        return render(request, 'pases.html', {'pases': pases}, context_instance=RequestContext(request))


    # Se persiste un Pase
    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def savePase(request):
                 
        pase = Pase()
          
        pase.numero = (request.POST.get('numero'))
           
        pase.departamento_origen = Departamento.objects.get(codigo=int (request.POST.get('departamento_origen')))
         
        pase.departamento_destino = Departamento.objects.get(codigo=int (request.POST.get('departamento_destino')))
               
        fecha = (request.POST.get('fecha'))
                      
        pase.fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")

        if((request.POST.get('expediente_tipo') == 'Expediente')):
            pase.expediente = Expediente.objects.get(id=int (request.POST.get('expediente_id')))
        else:
            pase.expediente = ExpedienteLey.objects.get(id=int (request.POST.get('expediente_id')))
        
        pase.estado = Estado.PENDIENTE.value
      
        pase.save()
      
        if(request.POST.get('expediente_tipo') == 'Expediente'):
            return ExpedientesView.showExpediente(request, request.POST.get('expediente_tipo'), pase.expediente.organismo, pase.expediente.numero, pase.expediente.anio, 0, 0, pase.expediente.alcance)
        else:  
            return ExpedientesView.showExpediente(request, request.POST.get('expediente_tipo'), pase.expediente.organismo, pase.expediente.numero, pase.expediente.anio, pase.expediente.partido.id, pase.expediente.region, pase.expediente.alcance)
            
         # TODO   
    def removePase(request):

        return ExpedientesView.showExpediente(request, request.POST.get('Expediente'), request.POST.get('expediente_id'))


    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def aceptarPase(request, idPase):
        
        pase = Pase.objects.get(id=idPase)
        pase.estado = Estado.ACEPTADO.value
        pase.save()
        
        return PasesView.getPases(request)

                
    def paginador(request, object):
        paginator = Paginator(object, 25)  # Show 25 contacts per page
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
        
            
            
    
'''
Crea y persiste un pase con origen y destino; lo asocia también al
expediente del parámetro
'''
def guardar_pase( origen, destino, expediente ):

    nuevo_pase = Pase()
    nuevo_pase.departamento_origen = origen 
    nuevo_pase.departamento_destino = destino
    now = datetime.datetime.now()
    nuevo_pase.fecha = now  
    nuevo_pase.estado = Estado.ACEPTADO.value
    nuevo_pase.expediente = expediente  
    nuevo_pase.save()
