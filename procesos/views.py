from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.core.context_processors import request
from django.http.response import HttpResponse
from django.template import RequestContext 




# Create your views here.
class ProcesosView(ListView):
    
    
    def inicio(request):
        
        return render(request, 'proceso.html', {},context_instance=RequestContext(request))
