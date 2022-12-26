
from rest_framework import serializers 

from .models import Student

class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

    def update(self,instance,validated_data):
        print(f"instance name---------{instance.name}")
        instance.name=validated_data.get('name',instance.name)
        print(f"instance name after ---------{instance.name}")
        instance.roll=validated_data.get('roll',instance.roll)
        print(f"instance city ---------{instance.city}")
        instance.city=validated_data.get('city',instance.city)
        print(f"instance city ---------{instance.city}")
        instance.save()
        return instance