from django.contrib import admin
from documentos.models import Expediente, ExpedienteLey, Pase

class PaseInLine(admin.TabularInline):
	model = Pase
	extra = 0
	
class ExpedienteAdmin(admin.ModelAdmin):
	search_fields = ['caracteristica','partido__nombre', 'region', 'numero', 'fecha', 'alcance', 'cuerpo']
	fieldsets = [
	(None, {'fields': ['caracteristica']}),
	(None, {'fields': ['partido']}),
	(None, {'fields': ['region']}),
	(None, {'fields': ['numero']}),
        (None, {'fields': ['fecha']}),
	(None, {'fields': ['alcance']}),
	(None, {'fields': ['cuerpo']})
	]	
	inlines = [PaseInLine]
	list_display = ('caracteristica', 'partido', 'region', 'numero', 'fecha' ,'alcance',  'cuerpo')
    
    
admin.site.register(Expediente)
admin.site.register(ExpedienteLey, ExpedienteAdmin)
admin.site.register(Pase)
