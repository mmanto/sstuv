from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from secur.views import LoginView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from documentos import documentos_sites
from comun import comun_sites
from publicador import publicador_sites
from procesos import procesos_sites
# from secur import secur_sites
from django.conf.urls.static import static

urlpatterns = patterns('',
                   url(r'^sig/auth/login/$','django.contrib.auth.views.login' , {'template_name': 'login.html'}),
                   url(r'^sig/auth/home/$', LoginView.home),
                   url(r'^sig/auth/logout/$', LoginView.logout, name='logout_view' ),
                   #url(r'^$', LoginView.home),
                   url(r'^sig/$', LoginView.home),
                   url(r'^admin/', include(admin.site.urls)),
                   #url(r'^static/(.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),

                   #ExpedienteLey
                   url(r'^sig/', include(documentos_sites)),
                      
                   #Pase 
                                    
                  url(r'^sig/', include(publicador_sites))  ,     
                  
                  
                  #Procesos                                     
                  url(r'^sig/', include(procesos_sites))  ,
                  
 
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
