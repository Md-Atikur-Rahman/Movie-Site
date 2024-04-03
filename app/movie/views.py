# movies/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, MovieRatings
from .forms import MovieForm, MovieRatingForm


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MovieForm()
    return render(request, 'movie/add_movie.html', {'form': form})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user_rating = None
    if request.method == 'POST':
        form = MovieRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.movie = movie
            rating.user = request.user
            rating.save()
            return redirect('movie_detail', movie_id=movie_id)
    else:
        form = MovieRatingForm()
        user_rating = MovieRatings.objects.filter(
            movie=movie, user=request.user).first()
    return render(request, 'movie/movie_detail.html', {
        'movie': movie,
        'form': form,
        'user_rating': user_rating
    })
