
from django.conf.urls import *

from comun.views import ImportView

urlpatterns = patterns('',
                        url(r'^partidos/importar/$', ImportView.importar),
                      )
        

