from django.conf import settings
from django.db import transaction
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from movie.models import Movie


@login_required
def dashboard(request):

    if 'q' in request.GET:
        query = request.GET['q']
        movies = Movie.objects.filter(name__icontains=query)
        return render(request, 'common/dashboard.html', {'movies': movies, 'query': query})
    else:
        movies = Movie.objects.all()

    paginator = Paginator(movies, 10)  # Show 10 movies per page.
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)

    return render(request, 'common/dashboard.html', {
        'movies': movies,
    })
