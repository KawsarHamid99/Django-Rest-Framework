from rest_framework import serializers
from .models import Teacher

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['id','name','roll','dept']
       
        
    