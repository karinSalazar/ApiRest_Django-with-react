from .models import Citas
from .serializers import CitaSerializer
from rest_framework import generics


class CitasListCreate(generics.ListCreateAPIView):
    queryset = Citas.objects.all()
    serializer_class = CitaSerializer