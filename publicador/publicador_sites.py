from django.conf.urls import *

from publicador.views import ArticulosView

urlpatterns = patterns('',
                        url(r'^publicador/inicio/$', ArticulosView.inicio),
                        url(r'^publicador/nuevo/(\d+)/$', ArticulosView.showArticulo),
                        url(r'^publicador/editar/(\d+)/$', ArticulosView.showArticulo),
                        url(r'^publicador/guardarEditado/$', ArticulosView.updateArticulo),
                        url(r'^publicador/guardar/$', ArticulosView.saveArticulo),
                        url(r'^publicador/buscaXTitulo/$', ArticulosView.buscarPorTitulo),
                      )
        