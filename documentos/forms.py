from documentos.models import Expediente, ExpedienteLey, Pase
from django.forms.models import ModelForm

class ExpedienteForm(ModelForm):

    class Meta:
       model = Expediente
       exclude = ['usuarioAlta']

    
class ExpedienteLeyForm(ExpedienteForm):
   
    class Meta:
        model = ExpedienteLey
        
        
        
        
class PaseForm(ModelForm):

    class Meta:
       model = Pase


        