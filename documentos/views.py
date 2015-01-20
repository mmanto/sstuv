from django.shortcuts import render


from django.views.generic import ListView
from documentos.models import ExpedienteLey, Expediente
from django.core.context_processors import request
from documentos.forms import ExpedienteLeyForm, ExpedienteForm
from comun.models import Partido, Departamento
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.http import HttpResponseRedirect

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
            return render(request, 'expediente_ley.html', {'expediente': expediente, 'partidos': partidos, 'departamentos':departamentos, 'tipo':tipo})
      
        else:
            return render(request, 'expediente_ley.html', {'partidos': partidos, 'departamentos':departamentos, 'tipo':tipo})
        
    
 
    def loadBusquedaExpediente(request):
        return render(request, 'expedienteley_list.html', {'tipo' : 'Expediente'})
    

    def loadBusquedaExpedienteLey(request):
        return render(request, 'expedienteley_list.html', {'tipo' : 'ExpedienteLey'})

    def showResultados(request, tipo):

        expedientes= []
        if 'id' in request.GET:
            
#             id= int(request.GET['id'],0)
    
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
     
        return render(request, 'expedienteley_list.html', {'expedientes' : expedientes, 'tipo' : tipo })

    
         
    
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
        
        return render(request, 'expedienteley_list.html',{'tipo' : tipo})
        

    def get_queryset(self):
        return ExpedienteLey.objects.all()

