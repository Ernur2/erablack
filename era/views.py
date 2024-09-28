from rest_framework import generics, viewsets
from .MainSerializer import MainSerializer

from .models import era


class MainViewSet(viewsets.ModelViewSet):
    queryset = era.objects.all()
    serializer_class = MainSerializer






# Create your views here.
