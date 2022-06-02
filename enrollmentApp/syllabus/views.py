from .serializer import SyllabusSerializer
from .models import Syllabus
from rest_framework import generics

class SyllabusViewList(generics.ListCreateAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer

class SyllabusViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer