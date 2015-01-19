from documentos.models import Expediente, ExpedienteLey
from django.forms.models import ModelForm


class ExpedienteForm(ModelForm):
   
    class Meta:
        model = Expediente
        
        
class ExpedienteLeyForm(ExpedienteForm, ModelForm):
   
    class Meta:
        model = ExpedienteLey