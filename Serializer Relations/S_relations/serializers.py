from .models import Singer,Song
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    #song=serializers.StringRelatedField(many=True,read_only=True)
    #song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail') #Not Working
    #song=serializers.SlugRelatedField(many=True,read_only=True,slug_field='duration') 
    #song=serializers.SlugRelatedField(many=True,read_only=True,slug_field='title') 
    class Meta:
        model=Singer
        fields=['id','name','gender','song']



#HyperLinkedModelSerializer
class Hyper_Linked_Model_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Singer
        fields=["id","url","name","gender"]

class Nasted_Serializer(serializers.ModelSerializer):
    song=SongSerializer(many=True,read_only=True)
    class Meta:
        model=Singer
        fields=["id","name","gender","song"]