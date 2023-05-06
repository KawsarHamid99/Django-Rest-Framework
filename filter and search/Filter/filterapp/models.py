from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)