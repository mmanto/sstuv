from publicador.models import Articulo
from django.forms.models import ModelForm
from django.forms import forms
from django.forms import DateInput, DateField


class ArticuloForm(ModelForm):

    class Meta:
       model = Articulo
        