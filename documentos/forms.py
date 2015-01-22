from documentos.models import Expediente, ExpedienteLey
from django.forms.models import ModelForm
from django.forms import forms
from django.forms import DateInput, DateField

class ExpedienteForm(ModelForm):
   

#     fecha = forms.DateField(widget=forms.DateInput(format = '%m/%d/%Y'), 
#                                input_formats=('%m/%d/%Y',), )    
   
    class Meta:
       model = Expediente
       

        
        
        
class ExpedienteLeyForm(ExpedienteForm):
   
    class Meta:
        model = ExpedienteLey