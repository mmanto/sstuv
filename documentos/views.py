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

            pases= expediente.pase_set.all()


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
                
            if form.is_valid():
                form.save()   
            else:
    #             form_errors = form.erros 
                return render(request, 'expedienteley_list.html',{'tipo' : tipo})
        
        return render(request, 'expedienteley_list.html',{'tipo' : tipo}, context_instance=RequestContext(request))
        

    def updateExpediente(request):
    
            tipo= request.POST.get('tipo','')
            numero =request.POST.get('numero','')
            
        
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
  
  
  
  
        
    def get_queryset(self):
        return ExpedienteLey.objects.all()






class PasesView(ListView):
    
    
    #Se persiste un Pase    
    def savePase(request):
      
        form=PaseForm(request.POST)
        
        if form.is_valid():  
                   
            form.save() 
            
            return render(request, 'expediente_ley.html')
    
            
            
            
            
            
            
            
            
            
            
            
    