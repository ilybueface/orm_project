from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    def __str__(self):
        return f'{self.first_name} |  {self.last_name} | {self.birth_year}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f'{self.title} | {self.author} | {self.genre}'


class Genre(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return f'{self.name}'