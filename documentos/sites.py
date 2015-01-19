from django.conf.urls import *
import documentos
from documentos.views import  LoginView, ExpedientesView

urlpatterns = patterns('',
    url(r'^expedientes/$', ExpedientesView.as_view()),  
    url(r'^expedientes/$', ExpedientesView.loadBusquedaExpediente),
    url(r'^expedientes/buscar/$', ExpedientesView.showResultados),
    url(r'^expediente/inspeccionar/(\d+)/$',ExpedientesView.showExpediente),
    url(r'^guardar/$', ExpedientesView.saveExpediente),
    url(r'^nuevo/(\d+)/$', ExpedientesView.showExpediente)

)
