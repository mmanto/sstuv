


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sstuv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^admin/', include(admin.site.urls))
#     url(r'^expedientes/$',ListView.as_view(queryset = ExpedienteLey.objects.all(),
#                                            template_name = 'expedienteley_list.html' ))



#     url(r'^expedientes/$', PostListView.as_view()) ,
#     url(r'^expedientes/', include('documentos.urls'))

)