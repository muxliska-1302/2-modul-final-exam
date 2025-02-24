from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    contact_email = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name