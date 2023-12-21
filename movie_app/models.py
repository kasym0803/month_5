from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=55, null=True, blank=True)


class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    duration = models.IntegerField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)


class Review(models.Model):
    text = models.CharField(max_length=156)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)


