from rest_framework import serializers
from documentos.models import Expediente
 
class ExpedienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expediente
        fields = ('organismo', 'numero', 'fecha_inicio',)