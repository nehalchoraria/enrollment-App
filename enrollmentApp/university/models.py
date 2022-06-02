from django.db import models

class University(models.Model):
    university_name = models.CharField(max_length=30)

    def __str__(self):
       return self.university_name
  