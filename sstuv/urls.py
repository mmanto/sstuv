from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from documentos.views import LoginView
from documentos import sites




urlpatterns = patterns('',
                   url(r'^sig/auth/login/$','django.contrib.auth.views.login' , {'template_name': 'login.html'}),
                   url(r'^sig/auth/home/$', LoginView.home),
                   url(r'^auth/logout/$', LoginView.logout, name='logout_view' ),
                   url(r'^$', LoginView.home),
                   url(r'^admin/', include(admin.site.urls)),

                   #ExpedienteLey
                   url(r'^sig/', include(sites)),   
        
                   #Pase     


)
