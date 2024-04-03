
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

from core.utils import load_movies, load_movie_ratings
from movie.models import Movie, MovieRatings
from movie.tasks import schedule_task


class Command(BaseCommand):
    help = 'Creates a user'

    def handle(self, *args, **kwargs):
        movies = load_movies()
        cc = 0
        for movie in movies:
            _, created = Movie.objects.get_or_create(
                name=movie["name"],
                genre=movie["genre"],
                rating=movie["rating"],
                release_date=datetime.strptime(
                    movie["release_date"], "%d-%m-%Y").date()
            )
            if created:
                cc += 1
        print(f"{cc} movie added")

        ratings = load_movie_ratings()
        cc = 0
        for rating in ratings:
            _, created = MovieRatings.objects.get_or_create(
                user=User.objects.get(id=rating['user_id']),
                movie=Movie.objects.get(id=rating['movie_id']),
                rating=rating['rating']
            )
            if created:
                cc += 1
        print(f"{cc} ratings added")
        print(schedule_task())
