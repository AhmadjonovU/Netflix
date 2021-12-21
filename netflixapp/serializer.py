from django.db.models import fields
from rest_framework import serializers
from .import models
from rest_framework.exceptions import ValidationError

class ActorListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Actor
        fields = ('id','name','birth_date','gender')
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ('id','name','year','imdb','genre','actor')
    def validate_imdb(self,qiymat):
        if qiymat < 2:
            raise ValidationError(detail='bunday kino mavjud emas')
        return qiymat

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('id','movie','user','text','created_date')
    def validate_text(self,text): 
        a = "yaramas"
        if a in text:
            raise ValidationError(detail="haqiqiqatni yozganiz uchun raxmat")
        return text

    
      