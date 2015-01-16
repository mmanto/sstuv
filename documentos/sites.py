from django.conf.urls import *
import documentos
from documentos.views import ExpedientesView, LoginView

# Admin-site-wide views.
urlpatterns = patterns('',
    #url(r'^/$', LoginView.as_view()),
    url(r'^expedientes/$', ExpedientesView.as_view()),  
    #url(r'^login/$', self.login, name='login'),
    #url(r'^logout/$', wrap(self.logout), name='logout'),
    #rl(r'^password_change/$', wrap(self.password_change, cacheable=True), name='password_change'),
    #url(r'^password_change/done/$', wrap(self.password_change_done, cacheable=True), name='password_change_done'),
    #url(r'^jsi18n/$', wrap(self.i18n_javascript, cacheable=True), name='jsi18n'),
    #url(r'^r/(?P<content_type_id>\d+)/(?P<object_id>.+)/$', wrap(contenttype_views.shortcut), name='view_on_site'),
)

# Add in each model's views, and create a list of valid URLS for the
# app_index

