from django.db import models
from course.models import CourseSyllabusMapping

# Create your models here.
class Student(models.Model):
    courseSyllabusMapping = models.ForeignKey(CourseSyllabusMapping, on_delete=models.CASCADE)
    enrollmentId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

