from dataclasses import fields
from .serializer import UniversitySerializer
from .models import University
from rest_framework import generics


class UserViewList(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UserViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer