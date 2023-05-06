from .models import Teacher
from rest_framework import serializers

class TeacherSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=["id","name","dept","state"]