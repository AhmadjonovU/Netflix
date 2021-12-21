from django.contrib.auth.models import User
from django.db import models

class Actor(models.Model):
    jinsi = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=jinsi)
    def str(self):
        return f"{self.name}"

class Movie(models.Model):
    janrlar = [
        ("Action", "Action"),
        ("Drama", "Drama"),
        ("Comedy", "Comedy"),
        ("Horror", "Horror"),
    ]
    def str(self):
        return f"{self.name}"

    name = models.CharField(max_length=50)
    year = models.DateField()
    imdb = models.FloatField()
    genre = models.CharField(max_length=30, choices=janrlar)
    actor = models.ManyToManyField(Actor)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)
    created_date = models.DateField(auto_now_add=True)
    def str(self):
        return f"{self.user.username}: {self.text}"

