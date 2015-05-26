
from django.conf.urls import *
from comun.views import ImportView
from comun import rest
from rest_framework.routers import DefaultRouter
from comun.rest import PartidoService, BarrioService


router = DefaultRouter()
router.register(r'partido', PartidoService,  base_name='partido')
router.register(r'barrio', BarrioService,  base_name='barrio')

urlpatterns = patterns('',
                        url(r'^partidos/importar/$', ImportView.importar),
                        
                        
                        
                        url(r'^', include(router.urls)),
                      )
        

