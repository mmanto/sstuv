from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from documentos.views import LoginView
from documentos import sites
from django.conf import settings



urlpatterns = patterns('',
                   url(r'^sig/auth/login/$','django.contrib.auth.views.login' , {'template_name': 'login.html'}),
                   url(r'^sig/auth/home/$', LoginView.home),
                   url(r'^auth/logout/$', LoginView.logout, name='logout_view' ),
                   url(r'^$', LoginView.home),
                   url(r'^admin/', include(admin.site.urls)),
                   url(r'^static/(.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),

                   #ExpedienteLey
                   url(r'^sig/', include(sites)),   
        
                   #Pase     


)
