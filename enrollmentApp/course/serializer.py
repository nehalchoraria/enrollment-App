from rest_framework import serializers
from .models import Course, CourseSyllabusMapping

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseSyllabusMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSyllabusMapping
        fields = '__all__'