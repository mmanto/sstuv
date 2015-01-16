from django.shortcuts import render


from django.views import generic
from documentos.models import ExpedienteLey, Expediente
from django.core.context_processors import request
from documentos import forms
from comun.models import Partido, Departamento



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
        
        id= int(request.GET['id'],0)

#         if id == 0 :   
#             expedientes = ExpedienteLey.objects.all()
#         else :
        if(tipo == 'ExpedienteLey'):
           if(ExpedienteLey.objects.filter(numero=id).exists()):         
                expedientes.append(ExpedienteLey.objects.get(numero=id))
        else:    
             if(Expediente.objects.filter(numero=id).exists()):         
                expedientes.append(Expediente.objects.get(numero=id))

            
 
 
    return render(request, 'expedienteley_list.html', {'expedientes' : expedientes, 'tipo' : tipo })

     
   
    
def saveExpediente(request):
    
    
    if request.method == 'POST':
        form = ExpedienteLeyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            #  TODO persistir         
            
    else:
        form = ContactForm()
    
    
    return render(request, 'expedienteley_list.html')
    
    
        
