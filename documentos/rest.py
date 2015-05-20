from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view
from documentos.serializers import ExpedienteSerializer
from documentos.models import Expediente, Estado
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response


class ExpedienteViewSet(ModelViewSet):
      
    serializer_class = ExpedienteSerializer   
    queryset = Expediente.objects.all()
 
 
     #http://localhost:8000/sig/exped/
    def list(self,request):
        print("entro la get")
   
        filter_dict = {}

        organismo = ExpedienteViewSet.toInt(request.GET['organismo'])
        numero = ExpedienteViewSet.toInt(self.request.GET['numero'])
        fecha_inicio = ExpedienteViewSet.toInt(self.request.GET['fecha_inicio'])
#         buscarExpPropios=(self.request.GET['radio'],0)
#         filter_dict['alcance'] = alcance = self.toInt(self.request.GET['alcance'])
          
        if (organismo > 0):
            filter_dict['organismo'] = organismo
        if (numero > 0):
            filter_dict['numero'] = numero
        if (fecha_inicio > 0):
            filter_dict['fecha_inicio'] = fecha_inicio

        if(len(filter_dict) > 0):
            queryset =  Expediente.objects.filter(**filter_dict)
        else:    
             queryset = Expediente.objects.all()  
        
        serializer_class = ExpedienteSerializer(queryset, many=True)  
        
        print(serializer_class.data)
        
        print("enviando respuesta")
        return Response (serializer_class.data)    

    
    
    
    
    
    
    
  
#     Utilitario    
    def toInt(valor):
        
        try: 
            print(valor)
            x = int(valor)
        except ValueError:
            x = 0
        return x    
