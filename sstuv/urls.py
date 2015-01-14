from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.list import ListView

from documentos.models import ExpedienteLey
import documentos

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sstuv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^expedientes/$',ListView.as_view(queryset = ExpedienteLey.objects.all(),
                                           template_name = 'expedienteley_list.html' ))    
)
