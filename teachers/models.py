from django.db import models
from departments.models import Department


class Teacher(models.Model):

    EMPLOYMENT_TYPES = [
        ('select employment type', 'Select employment type'),
        ('full time', 'Full time'),
        ('part time', 'Part time'),
        ('contract', 'Contract'),
    ]

    photo = models.ImageField(upload_to='teachers-photos/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')
    position = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    join_date = models.DateField()
    subjects = models.ManyToManyField('subjects.Subject', related_name='teachers')
    employment_type = models.CharField(max_length=100, choices=EMPLOYMENT_TYPES, default='select employment type')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"