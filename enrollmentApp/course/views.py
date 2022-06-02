from .serializer import CourseSerializer, CourseSyllabusMappingSerializer
from .models import Course, CourseSyllabusMapping
from rest_framework import generics

class CourseViewList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseSyllabusMappingViewList(generics.ListCreateAPIView):
    queryset = CourseSyllabusMapping.objects.all()
    serializer_class = CourseSyllabusMappingSerializer

class CourseSyllabusMappingViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseSyllabusMapping.objects.all()
    serializer_class = CourseSyllabusMappingSerializer