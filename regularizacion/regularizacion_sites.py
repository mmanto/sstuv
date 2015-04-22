from django.conf.urls import *
from regularizacion.views import CensoView



urlpatterns = patterns('',
            
                  #Censo
                  url(r'^censo/nuevo/$', CensoView.nuevo),
                  
                  url(r'^censo/guardar/$', CensoView.guardar),

                    )
