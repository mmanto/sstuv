from documentos.models import Expediente, ExpedienteLey, Pase
from django.forms.models import ModelForm
from django.forms import forms
from django.forms import DateInput, DateField

class ExpedienteForm(ModelForm):

    class Meta:
       model = Expediente
       

    
class ExpedienteLeyForm(ExpedienteForm):
   
    class Meta:
        model = ExpedienteLey
        
        
        
        
class PaseForm(ModelForm):

    class Meta:
       model = Pase


        