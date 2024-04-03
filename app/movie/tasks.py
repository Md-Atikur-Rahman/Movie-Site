import json
from time import sleep
from celery import shared_task
from django.conf import settings
from django.db.models import Avg
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .models import Movie, MovieRatings


@shared_task
def generate_ratings():
    movies = Movie.objects.all()
    for movie in movies:
        average_rating = MovieRatings.objects.filter(
            movie=movie).aggregate(Avg('rating'))['rating__avg']
        movie.average_rating = average_rating
        movie.save()
    # return "Task Complete!"


def schedule_task():
    interval, _ = IntervalSchedule.objects.get_or_create(
        every=15,
        period=IntervalSchedule.SECONDS
    )

    PeriodicTask.objects.create(
        interval=interval,
        name='generateAverageRating',
        task="movie.tasks.generate_ratings",
        # args=json.dumps(["Arg1", "Arg2"])
        # one_off=True
    )
    return "Task Scheduled!"
