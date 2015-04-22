from django.conf.urls import *
from procesos.views import ProcesosView
from regularizacion import regularizacion_sites

urlpatterns = patterns('',
                       url(r'^inicio/$', ProcesosView.inicio),
                       
                    
                        url(r'^regularizacion/', include(regularizacion_sites))  ,




                      )
        