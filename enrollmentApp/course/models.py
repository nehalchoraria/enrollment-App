from django.db import models
from university.models import University
from syllabus.models import Syllabus

# Create your models here.
class Course(models.Model):
    universityId = models.ForeignKey(University, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class CourseSyllabusMapping(models.Model):
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    syllabusId = models.ForeignKey(Syllabus, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        unique_together = ('courseId', 'syllabusId')
