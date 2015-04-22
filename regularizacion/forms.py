from django.forms.models import ModelForm
from regularizacion.models import Censo

class CensoForm(ModelForm):

    class Meta:
       model = Censo
       
