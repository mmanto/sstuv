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
    #model = ExpedienteLey.objects.all()
    template_name = 'expedienteley_list.html'
    paginate_by = 10
    
    def showExpediente(request, tipo, id):
    
        id= int(id)
            
        partidos =  Partido.objects.all()
       
        departamentos=Departamento.objects.all()
        
        #Si el id es 0 es uno nuevo
        if(id != 0):
            
            if(tipo == 'ExpedienteLey'):
                expediente = ExpedienteLey.objects.get(numero=id)
            else:
                expediente = Expediente.objects.get(numero=id)

            pases = expediente.pase_set.all()


            return render(request, 'expediente_ley.html', {'expediente': expediente, 'partidos': partidos, 'departamentos':departamentos, 'tipo':tipo, 'accion':'editar', 'pases':pases}, context_instance=RequestContext(request) )
      
        else:
            return render(request, 'expediente_ley.html', {'partidos': partidos, 'departamentos':departamentos, 'tipo':tipo, 'accion':'nuevo'},context_instance=RequestContext(request))
        
    
 
    def loadBusquedaExpediente(request):
        return render(request, 'expedienteley_list.html', {'tipo' : 'Expediente'}, context_instance=RequestContext(request))
    

    def loadBusquedaExpedienteLey(request):
        return render(request, 'expedienteley_list.html', {'tipo' : 'ExpedienteLey'}, context_instance=RequestContext(request))

    def showResultados(request, tipo):

        expedientes= []
        if 'id' in request.GET:
       
            if request.GET['id'] =='' or request.GET['id'] == '0'  :
                expedientes = Expediente.objects.all()
            else :
             
                try:
                
                    id= int(request.GET['id'],0)
    
                    if(tipo == 'ExpedienteLey'):
                       if(ExpedienteLey.objects.filter(numero=id).exists()):         
                            expedientes.append(ExpedienteLey.objects.get(numero=id))
                    else:    
                         if(Expediente.objects.filter(numero=id).exists()):         
                            expedientes.append(Expediente.objects.get(numero=id))
                except:         
                    expedientes= []
         
        paginator = Paginator(expedientes, 25) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            expedientes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            expedientes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            expedientes = paginator.page(paginator.num_pages)           
        
        return render_to_response('expedienteley_list.html', {'expedientes' : expedientes, 'tipo' : tipo }, context_instance=RequestContext(request))
    
    def saveExpediente(request):
    
        tipo= request.POST.get('tipo','')
    
        if request.method == 'POST':
            
            if(tipo == 'Expediente'):
                form = ExpedienteForm(request.POST)
            else:
                
                
                form = ExpedienteLeyForm(request.POST)
                
                form.model.partido = Departamento.objects.get( codigo = int (request.POST.get('partido')))

                
            if form.is_valid():
                form.save()   
            else:
    #             form_errors = form.erros 
                return render(request, 'expedienteley_list.html',{'tipo' : tipo})
        
        return render(request, 'expedienteley_list.html',{'tipo' : tipo}, context_instance=RequestContext(request))
        

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


class PasesView(ListView):
    
    
    #Se persiste un Pase    
    def savePase(request):
                 
        pase = Pase()
           
        pase.departamento_origen = Departamento.objects.get( codigo = int (request.POST.get('departamento_origen')))
         
        pase.departamento_destino = Departamento.objects.get( codigo = int (request.POST.get('departamento_destino')))
                                  
        fecha= (request.POST.get('fecha'))
        
        fecha1 =   datetime.strptime( fecha, "%d/%m/%Y" )
                           
        pase.fecha =  datetime.strptime( fecha, "%d/%m/%Y" )

        pase.expediente = Expediente.objects.get( numero = int (request.POST.get('expediente_id')))
      
        pase.save()
      
        return ExpedientesView.showExpediente(request, request.POST.get('Expediente'), request.POST.get('expediente_id'))

            
            
    def removePase(request):

        return ExpedientesView.showExpediente(request, request.POST.get('Expediente'), request.POST.get('expediente_id'))

            
            
            
            
            
            
    