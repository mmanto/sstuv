from django.conf.urls import *
from procesos.views import ProcesosView
from regularizacion import regularizacion_sites

urlpatterns = patterns('',
                       #url(r'^regu/inicio/$', ProcesosView.inicio),
                        
                        #Import urls  regularizacion                                     
                        url(r'^regu/', include(regularizacion_sites))  ,


                      )
        