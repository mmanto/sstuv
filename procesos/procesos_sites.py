from django.conf.urls import *
from procesos.views import ProcesosView


urlpatterns = patterns('',
                       url(r'^proc/inicio/$', ProcesosView.inicio),
                        


                      )
        