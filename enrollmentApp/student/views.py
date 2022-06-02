from .serializer import StudentSerializer
from .models import Student
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student.models import Student
from student.serializer import StudentSerializer

class StudentViewList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

@api_view(['GET'])
def findStudents(request):
    courseId = request.query_params.get('courseId')
    syllabusId = request.query_params.get('syllabusId')
    enrollmentId = request.query_params.get('enrollmentId')

    students = Student.objects
    
    # Filtering based on enrollment Id
    if(enrollmentId != None):
        students = students.filter(enrollmentId = enrollmentId)

    if(syllabusId != None):
        students = students.filter(courseSyllabusMapping__syllabusId = syllabusId)

    if(courseId != None):
        students = students.filter(courseSyllabusMapping__courseId = courseId)
    
    serializer = StudentSerializer(students.all(), many=True)
    return Response(serializer.data)