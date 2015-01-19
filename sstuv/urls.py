from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from documentos import views




urlpatterns = patterns('',

   
    url(r'^admin/', include(admin.site.urls)),
    
    
    #ExpedienteLey     
    
    url(r'^expedientesLey/$', views.loadBusquedaExpedienteLey),
    url(r'^expedientes/$', views.loadBusquedaExpediente),
   
        
    url(r'^buscar/(.*)/$', views.showResultados),
    url(r'^inspeccionar/(.+)/(\d+)/$', views.showExpediente),
    url(r'^guardar/$', views.saveExpediente),
    url(r'^nuevo/(.+)/(\d+)/$', views.showExpediente)

    
    #Pase     


)
