from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=20, default='')
    def __str__(self):
        return f'{self.id}: {self.name}'

class Movie(models.Model):
    title = models.TextField()
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre,on_delete=models.SET_DEFAULT,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.id}: {self.title} , {self.genre.name}'

class Score(models.Model):
    content = models.CharField(max_length=80, default='')
    score = models.IntegerField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.id}: {self.movie.title}/ {self.content}/ {self.score}'