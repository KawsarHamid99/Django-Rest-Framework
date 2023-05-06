from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.PositiveIntegerField(unique=True)
    dept=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="serializer")

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    dept=models.CharField(max_length=100)
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)