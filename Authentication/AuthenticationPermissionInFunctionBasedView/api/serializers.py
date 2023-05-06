from .models import Student
from rest_framework import serializers




class StudentSerializer(serializers.ModelSerializer):

    #validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("Name must be start with R")


    #name=serializers.CharField(read_only=True)
    #name=serializers.CharField(validators=[start_with_r])
    class Meta:
        model=Student
        fields=["id","name","roll","city"]
        #read_only_fileds=["name",'roll']
        #extra_kwargs={'name':{'read_only':True}}
    


    #Field Lavel Validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value

    # object lavel Validation
    def validate(self,data):
        nm=data.get("name",None)
        ct=data.get("city",None)
        if nm is not None and ct is not None:
            if nm.lower()=="rawsar" and ct.lower() != "kulna":
                raise serializers.ValidationError("City must be khulna")
        return data