import os
import csv
import json
import requests
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission

USERS_METADATA_CSV = os.path.join(settings.DATA_DIR, "users.csv")
MOVIES_METADATA_CSV = os.path.join(settings.DATA_DIR, "movies.csv")
MOVIES_RATINGS_METADATA_CSV = os.path.join(settings.DATA_DIR, "ratings.csv")


def load_users():
    dataset = []
    with open(USERS_METADATA_CSV, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = {
                'name':  row.get("name"),
                'phone':  row.get("phone"),
                'email':  row.get("email"),
                'password': row.get("password"),
            }
            dataset.append(data)
    return dataset


def load_movies():
    dataset = []
    with open(MOVIES_METADATA_CSV, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = {
                'name':  row.get("name"),
                'genre':  row.get("genre"),
                'rating':  row.get("rating"),
                'release_date': row.get("release_date"),
            }
            dataset.append(data)
    return dataset


def load_movie_ratings():
    dataset = []
    with open(MOVIES_RATINGS_METADATA_CSV, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = {
                'user_id':  int(row.get("user_id")),
                'movie_id':  int(row.get("movie_id")),
                'rating': int(float(row.get("rating"))),
            }
            dataset.append(data)
    return dataset
