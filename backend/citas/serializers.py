from rest_framework import serializers
from .models import Citas

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = ['id', 'autor', 'mensaje']