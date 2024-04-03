# movies/forms.py
from django import forms
from .models import Movie, MovieRatings


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'genre', 'rating', 'release_date']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }


class MovieRatingForm(forms.ModelForm):
    class Meta:
        model = MovieRatings
        fields = ['rating']
