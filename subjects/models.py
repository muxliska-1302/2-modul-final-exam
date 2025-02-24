from django.db import models
from departments.models import Department


class Subject(models.Model):

    GRADE_CHOICES = [
        ('select grade', 'Select Grade'),
        ('grade 9', 'Grade 9'),
        ('grade 10', 'Grade 10'),
        ('grade 11', 'Grade 11'),
        ('grade 12', 'Grade 12')
    ]

    PREREQUISITES_CHOICES = [
        ('basic mathematics', 'Basic mathematics'),
        ('introduction to physics', 'Introduction to physics'),
        ('basic chemistry', 'Basic chemistry'),
        ('english language', 'English language'),
    ]

    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')
    credit_hours = models.PositiveIntegerField()
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES, default='select grade')
    description = models.TextField()
    prerequisites = models.CharField(max_length=100, choices=PREREQUISITES_CHOICES)

    def __str__(self):
        return self.name
