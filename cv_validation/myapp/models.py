from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    roll=models.IntegerField()
    dept=models.CharField(max_length=100)
    