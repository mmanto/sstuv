from django.conf.urls import *

from documentos.views import ExpedientesView, PasesView
from documentos.report import PaseReport


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
                        


                      )
        