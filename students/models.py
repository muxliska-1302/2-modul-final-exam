from django.db import models


class Student(models.Model):

    GENDER_CHOICES = [
        ('select gender', 'Select gender'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    GRADE_CHOICES = [
        ('select grade', 'Select Grade'),
        ('grade 9', 'Grade 9'),
        ('grade 10', 'Grade 10'),
        ('grade 11', 'Grade 11'),
        ('grade 12', 'Grade 12')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='select gender')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, related_name='students')
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES, default='select grade')
    address = models.TextField()
    photo = models.ImageField(upload_to='students-photos/')
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15, unique=True)
    parent_email = models.EmailField(unique=True)
    relationship = models.CharField(max_length=100)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"