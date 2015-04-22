from django.shortcuts import render
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
import logging
logger = logging.getLogger('sstuvInfo')
loggerError = logging.getLogger('sstuvError')
from django.db.models import Q 
from django.db import connection


from django.views.generic import ListView
from documentos.models import Expediente
from comun.models import Partido, Departamento, Barrio




class CensoView(ListView):

    def nuevo(request):
        
        
        return render(request, 'censo.html', {'': partidos }, context_instance=RequestContext(request))
    
    def guardar(request):
        
        
        return render(request, 'censo.html', {'': partidos }, context_instance=RequestContext(request))
    

    def buscar(request):
        
        return render(request, 'censo_list.html', {'': partidos }, context_instance=RequestContext(request))

