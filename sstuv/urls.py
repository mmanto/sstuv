from django.conf.urls import patterns, include, url
from django.contrib import admin
from documentos.views import ExpedientesView, LoginView
from documentos.models import ExpedienteLey
from documentos import sites
from django.views.generic.base import RedirectView
from django.db.models import permalink


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sstuv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^sig/auth/login/$','django.contrib.auth.views.login' , {'template_name': 'login.html'}),
    url(r'^sig/auth/home/$', LoginView.home),
    #url(r'^auth/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/auth/login'}),
    url(r'^auth/logout/$', LoginView.logout, name='logout_view' ),
    #url(r'^auth/login/$', LoginView.home),
    #url(r'^$', LoginView.home),
    #url(r'^auth/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'admin/logged_out.html'}),
    #url(r'^$', RedirectView.as_view(url='/sig/auth/home', permanent = False)),
    url(r'^$', LoginView.home),
    url(r'^sig/', include(sites)),
    #url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^expedientes/$',ListView.as_view(queryset = ExpedienteLey.objects.all(),
    #                                       template_name = 'expedienteley_list.html' ))
    
    url(r'^sig/', include(sites)) 
)
