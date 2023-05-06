from serializerapp.models import Teacher
from rest_framework import serializers


class TeacherSrializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['id','name','roll','dept']