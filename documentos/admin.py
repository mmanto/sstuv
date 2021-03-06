from django.contrib import admin
from documentos.models import Expediente, ExpedienteLey, Pase

class PaseInLine(admin.TabularInline):
	model = Pase
	extra = 0
	
class ExpedienteAdmin(admin.ModelAdmin):
	search_fields = ['caracteristica','partido__nombre', 'region', 'numero', 'anio', 'alcance', 'cuerpo']
	fieldsets = [
	(None, {'fields': ['caracteristica']}),
	(None, {'fields': ['partido']}),
	(None, {'fields': ['region']}),
	(None, {'fields': ['numero']}),
        (None, {'fields': ['anio']}),
	(None, {'fields': ['alcance']}),
	(None, {'fields': ['cuerpo']})
	]	
	inlines = [PaseInLine]
	list_display = ('caracteristica', 'partido', 'region', 'numero', 'anio' ,'alcance',  'cuerpo')
    
    
    
class ExpAdmin(admin.ModelAdmin):
  fildsets= [
	(None, {'fields': ['caracteristica']}),
	(None, {'fields': ['numero']}),
        (None, {'fields': ['anio']}),
	(None, {'fields': ['alcance']}),
	(None, {'fields': ['cuerpo']})
    ]
  
  list_display = ('caracteristica', 'numero', 'anio' ,'alcance',  'cuerpo')
    
    
admin.site.register(Expediente, ExpAdmin)
admin.site.register(ExpedienteLey, ExpedienteAdmin)
admin.site.register(Pase)
