from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    release_date = models.DateField()
    average_rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ratings: {self.average_rating}"


class MovieRatings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ['user', 'movie']

    def __str__(self):
        return f"{self.movie.name} - {self.user.username}: {self.rating}"
