from django import forms

class ExpedienteLeyForm(forms.Form):
#     subject = forms.CharField()
#     email = forms.EmailField(required=False)
#     message = forms.CharField()
    
    numero = forms.IntegerField()
    fecha=forms.DateField(required=True)
    caracteristica=forms.CharField(required=True)
    alcance=forms.CharField()
    cuerpo=forms.CharField()