from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from netflixapp.models import Actor,Movie
from netflixapp.serializer import ActorListSerializer,CommentSerializer,MovieSerializer

class TestMovieList(TestCase):
    def setUp(self):
        self.cl = Client()
        self.actor = Actor.objects.create(name="raj Kapoor",gender="Male",birth_date="1956-11-12")
        self.movies = Movie.objects.create(name="Begubor",genre = "Comedy",imdb=6.9,year="1978-11-12")
        self.movies.actor.add(self.actor)
    def test_all_movies(self):
        movies = self.cl.get('/movie/').data
        print(movies)
        assert len(movies)==1
        assert movies[0]['id'] is not None
        assert movies[0]['name']=='Begubor'
        assert movies[0]['genre']=='Comedy'

class TestActorListCreateView(TestCase):
    def setUp(self):
        self.cl = Client()
    
    def test_post_an_actor(self):
        aktyor = {
            "id":1,
            "name":"Ulugbek Qodirov",
            "birth_date":"1985-12-05",
            "gender":"Male"
        }
        ak2 = {
            "id":1,
            "name":"Silvestr Stalone",
            "birth_date":"1956-12-13",
            "gender":"Male"
        }
        a = self.cl.post('/actors/',data=aktyor)
        b = self.cl.post('/actors/',data=ak2)
        assert a.status_code == 201
        assert b.status_code == 201
        actor = self.cl.get("/actors/").data
        assert actor is not None
        assert actor[0]['id'] is not None
        assert actor[0]['name'] == "Ulugbek Qodirov"
        assert actor[0]['gender'] == "Male"
        assert actor[0]['birth_date'] == '1985-12-05'
        assert actor[1]['id'] is not None
        assert actor[1]['name'] == "Silvestr Stalone"
        assert actor[1]['gender'] == "Male"
        assert actor[1]['birth_date'] == '1956-12-13'

class TestMovieListCreateView(TestCase):
    def setUp(self):
        self.cl = Client()
    
    def test_post_an_movie(self):
        aktyor = {
            "id":1,
            "name":"Ulugbek Qodirov",
            "birth_date":"1985-12-05",
            "gender":"Male"
        }
        a = self.cl.post('/actors/',data=aktyor)
        kino = {
            "id":1,
            "name":"Fribgarlar",
            "imdb":9.1,
            "year":"1985-12-05",
            "genre":"Comedy",
            "actor" : [1]
        }
        m1 = self.cl.post('/movie/',data=kino)
        assert m1.status_code == 201
        movies = self.cl.get("/movie/").data
        assert len(movies) > 0
        assert m1 is not None
        assert movies[0]['id'] is not None
        assert movies[0]['name'] == "Fribgarlar"
        assert movies[0]['genre'] == "Comedy"
        assert movies[0]['year'] == '1985-12-05'
        assert movies[0]['imdb'] == 9.1
