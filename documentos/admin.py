from django.contrib import admin
from documentos.models import Expediente, ExpedienteLey, Pase

class ExpedienteAdmin(admin.ModelAdmin):
    fieldsets = [
	(None, {'fields': ['caracteristica']}),
	(None, {'fields': ['partido']}),
	(None, {'fields': ['region']}),
	(None, {'fields': ['numero']}),
        (None, {'fields': ['fecha']}),
	(None, {'fields': ['alcance']}),
	(None, {'fields': ['cuerpo']})
    ]
    #inlines = [ChoiceInline]
    list_display = ('caracteristica', 'partido', 'region', 'numero', 'fecha' ,'alcance',  'cuerpo')
    
    
admin.site.register(Expediente)
admin.site.register(ExpedienteLey, ExpedienteAdmin)
admin.site.register(Pase)
