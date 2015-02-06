from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from documentos.views import LoginView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from documentos import documentos_sites
from comun import comun_sites


urlpatterns = patterns('',
                   url(r'^sig/auth/login/$','django.contrib.auth.views.login' , {'template_name': 'login.html'}),
                   url(r'^sig/auth/home/$', LoginView.home),
                   url(r'^auth/logout/$', LoginView.logout, name='logout_view' ),
                   url(r'^$', LoginView.home),
                   url(r'^admin/', include(admin.site.urls)),
                   #url(r'^static/(.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),

                   #ExpedienteLey
                   url(r'^sig/', include(documentos_sites)),
                      
                   url(r'^sig/', include(comun_sites))  ,   
        
                   #Pase     

)

urlpatterns += staticfiles_urlpatterns()
