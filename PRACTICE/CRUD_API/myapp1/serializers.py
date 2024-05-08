from rest_framework import serializers
from .models import Students

class StudentSerializers(serializers.ModelSerializer):
    def lessthen(value):
        if value <50:
            raise serializers.ValidationError("roll can not be less then 50")
    roll=serializers.IntegerField(validators=[lessthen])
    class Meta:
        model=Students
        fields=["id",'name','roll','city']
    def validate_roll(self,value):
        if value >100:
            raise serializers.ValidationError("roll can not be moew then 100")
        return value


    def validate(self, values):
        nm=values.get('name',None)
        ct=values.get('city',None)

        if nm[0].lower() == 'k' and ct[0].lower() == 'k':
            raise serializers.ValidationError("name and city can to start with k or K at  time")
        return values