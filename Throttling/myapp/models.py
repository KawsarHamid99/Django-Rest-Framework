from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=50)
    state=models.CharField(max_length=80)