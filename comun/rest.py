from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.request import HttpRequest
from django.http.response import HttpResponse
import requests
# from comun.model import Partido
 





class BarrioService(ModelViewSet):
      

 
    #http://localhost:8000/comun/barrio/
    def list(self,request):
          
        print("Ento al servicio BarrioService")   
        r= requests.get('')
     
        return HttpResponse( r, content_type="json")  
   
       

    
    
class PartidoService(ModelViewSet):
    
    partidos= []
    
    
    #http://localhost:8000/comun/partido/
    def list(self,request):
        
        print("Ento al servicio PartidoService")   
        r= requests.get('http://190.188.234.6/geoserver/wfs?srsName=EPSG%3A4326&typename=geonode%3Apartidos_pba_2014_cod_catastro&outputFormat=json&version=1.0.0&service=WFS&request=GetFeature')
     
        return HttpResponse( r, content_type="json")    
        
        
        
        
        
       