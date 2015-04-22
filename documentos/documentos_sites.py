from django.conf.urls import *

from documentos.views import ExpedientesView, PasesView
from documentos.report import PaseReport
from documentos.rest import ExpedienteViewSet
from documentos import rest

from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'exped', ExpedienteViewSet,  base_name='exped')
# router.register(r'exped/$', rest.list)



urlpatterns = patterns('',
                        url(r'^expedientesLey/$', ExpedientesView.loadBusquedaExpedienteLey),
                        url(r'^expedientes/$', ExpedientesView.loadBusquedaExpediente),
                        url(r'^expedientes/buscar/(.*)/$', ExpedientesView.showResultados),
                        url(r'^expediente/inspeccionar/(.*)/(\d+)/(\d+)/(\d+)/(\d+)/(.*)/(\d+)/$', ExpedientesView.showExpediente),
                        url(r'^expedientes/guardar/$', ExpedientesView.saveExpediente),
                        url(r'^expedientes/nuevo/(.+)/(\d+)/(\d+)/(\d+)/(\d+)/(.*)/(\d+)/$', ExpedientesView.showExpediente),
                        url(r'^expedientes/editar/$', ExpedientesView.updateExpediente),
                        url(r'^expedientes/importarExpedienteLey/$', ExpedientesView.importarExpedientesLey),
                        url(r'^expedientes/importarExpediente/$', ExpedientesView.importarExpedientes),    
                        
                        
                        url(r'^pases/$',PasesView.getPases ),
                        url(r'^pase/guardar/$', PasesView.savePase),
                        url(r'^pases/aceptar/(.*)/$', PasesView.aceptarPase),

                            
                        url(r'^expedientes/imprimirremito/(\d+)/(\d+)/$',PaseReport.generar ),
                        
#                          url(r'^exped/$', rest.get),
                        url(r'^', include(router.urls)),
#                         url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                        

                      )
        