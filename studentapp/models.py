from django.db import models

class Student(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} ({self.grade})"
