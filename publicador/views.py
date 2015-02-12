from django.shortcuts import render, render_to_response
from publicador import models
from django.views.generic import ListView
from pip._vendor.requests.models import Response
from django.template.loader import render_to_string
from django.contrib.gis.shortcuts import render_to_text
from django.http.response import HttpResponse
from publicador.models import Articulo
from django.template import RequestContext
from django.core.context_processors import request
from publicador.forms import ArticuloForm
from django.contrib.messages.tests.urls import show
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ArticulosView(ListView):
    
    def inicio(request):
        return ArticulosView.listarTodos(request)

    def listarTodos(request):
        articulos = Articulo.objects.all().order_by('id').reverse()
        articulos = ArticulosView.paginador(request, articulos)
        return render_to_response('listArticulos.html', {'articulos' : articulos, 'valorCampoTitulo': '' }, context_instance=RequestContext(request))
    
    def showArticulo(request, id):
    
        id= int(id)
                 
        #Si el id es 0 es uno nuevo
        if(id != 0):
            
            articulo = Articulo.objects.get(id=id)

            return render(request, 'articulo.html', {'articulo': articulo, 'accion':'editar'}, context_instance=RequestContext(request) )
      
        else:
            return render(request, 'articulo.html', {'accion':'nuevo'},context_instance=RequestContext(request))
        
    
    def saveArticulo(request):

        if request.method == 'POST':
            
            if "guardar" in request.POST:
                              
                form = ArticuloForm(request.POST)
            
                if form.is_valid():
                    form.save()   
                else:
                    return render(request, 'listArticulos.html')

        return ArticulosView.listarTodos(request)
        
        
    def updateArticulo(request):
    
        if "guardar" in request.POST:
            
            id = request.POST.get('id','')
            
            articulo = Articulo.objects.get(id = id)
            
            if request.method == 'POST':
                form = ArticuloForm(request.POST, instance=articulo)               
                if form.is_valid():  
                    form.save()
         
        return ArticulosView.listarTodos(request)
            
    def buscarPorTitulo(request):

        articulos= []
        if 'valorCampoTitulo' in request.GET:
       
            if request.GET['valorCampoTitulo'] == '':
                articulos = Articulo.objects.all().order_by('id').reverse()
            else :
             
                try:
                
                    valorCampoTitulo = request.GET['valorCampoTitulo']
    
                    if(Articulo.objects.filter(titulo__icontains = valorCampoTitulo).exists()):
                        articulos = Articulo.objects.filter(titulo__icontains = valorCampoTitulo).distinct().order_by('id').reverse()
                        '''
                            qset = (
                                    Q(titulo__icontains = valorCampoTitulo) 
                            )
                            articulos = Articulo.objects.filter(qset).distinct().order_by('id').reverse()
                        '''        
                            
                except:         
                    articulos = []
        
        articulos = ArticulosView.paginador(request, articulos)
        return render_to_response('listArticulos.html', {'articulos' : articulos, 'valorCampoTitulo': request.GET['valorCampoTitulo'] }, context_instance=RequestContext(request))

    def paginador(request, articulos):
        paginator = Paginator(articulos, 5) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            articulos = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articulos = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            articulos = paginator.page(paginator.num_pages)   
        return articulos