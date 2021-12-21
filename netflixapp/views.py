from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from netflixapp.serializer import MovieSerializer,CommentSerializer
from .models import*
from rest_framework import generics
from .serializer import ActorListSerializer
from rest_framework.filters import OrderingFilter, SearchFilter


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ["name",]
    ordering_fields = ["imdb"]

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer

class ActorList(generics.ListAPIView): 
    queryset = Actor.objects.all() 
    serializer_class =ActorListSerializer
    filter_backends = [SearchFilter,]
    search_fields = ["name","birth_date",]

class anActor(generics.RetrieveAPIView): 
    queryset = Actor.objects.all() 
    serializer_class = ActorListSerializer 

class CreateActor(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer

class DelateActor(generics.RetrieveDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer
 