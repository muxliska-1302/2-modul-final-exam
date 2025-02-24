
from django.db import models
from teachers.models import Teacher


class Group(models.Model):
    GRADE_CHOICES = [
        ('select grade', 'Select Grade'),
        ('grade 9', 'Grade 9'),
        ('grade 10', 'Grade 10'),
        ('grade 11', 'Grade 11'),
        ('grade 12', 'Grade 12')
    ]

    SCHEDULE_CHOICES = [
        ('select schedule', 'Select schedule'),
        ('morning session', 'Morning session'),
        ('afternoon session', 'Afternoon session'),
        ('evening session', 'Evening session'),
    ]

    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES, default='select grade')
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='group')
    schedule = models.CharField(max_length=100, choices=SCHEDULE_CHOICES, default='select schedule')
    academic_year = models.CharField(max_length=20)
    max_students = models.PositiveIntegerField()
    description = models.TextField()
    subjects = models.ManyToManyField('subjects.Subject', related_name='groups')

    def __str__(self):
        return self.name
