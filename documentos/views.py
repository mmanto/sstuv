from django.shortcuts import render


from django.views import generic
from documentos.models import ExpedienteLey
from django.core.context_processors import request
from documentos import forms
from comun.models import Partido, Departamento



def showExpediente(request, id):
    
    id= int(id)
    
    partidos =  Partido.objects.all()
   
    departamentos=Departamento.objects.all()
    
    if(id != 0):
        expediente = ExpedienteLey.objects.get(numero=id)
        return render(request, 'expediente_ley.html', {'expediente': expediente, 'partidos': partidos, 'departamentos':departamentos})

   
    else:
        return render(request, 'expediente_ley.html', {'partidos': partidos, 'departamentos':departamentos})
    
   
  
   
        


def loadBusquedaExpediente(request):
    
        return render(request, 'expedienteley_list.html')
    
    
def showResultados(request):
    
    expedientes= []
    if 'id' in request.GET:
        
        id= int(request.GET['id'],0)

        if not id:
            id=0

        if id == 0 :   
            expedientes = ExpedienteLey.objects.all()
        else :
            #Se verifica que el expediente exista             
             if(ExpedienteLey.objects.filter(numero=id).exists()):         
                expedientes.append(  ExpedienteLey.objects.get(numero=id))
 
    return render(request, 'expedienteley_list.html', {'expedientes' : expedientes})

     
    
def saveExpediente(request):
    
    
    if request.method == 'POST':
        form = ExpedienteLeyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            
    else:
        form = ContactForm()
    
    
    return render(request, 'expedienteley_list.html')
    
    
# def loadPartidos(request):
#    partidos= Partido.objects.all()
        
