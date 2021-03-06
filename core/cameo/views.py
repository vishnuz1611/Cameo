from django.http import response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from .models import MovieSeries, Genre, Rating, Watchlist
from django.utils.text import slugify

def index(request):
    query = request.GET.get('q')
    if query:
        url = 'http://www.omdbapi.com/?apikey=<your-api-key-here>&s=' + query
        response = requests.get(url)
        data = response.json()
        context = {
            'query' : query,
            'data' : data,
        }
        return render(request, 'results.html', context)

    info = MovieSeries.objects.all()
    context = {
        'info': info
    }
    return render(request, 'index.html', context)


def description(request, imdb_id):
    if MovieSeries.objects.filter(imdbID=imdb_id).exists():
        data = MovieSeries.objects.get(imdbID=imdb_id)
        in_db = True

    else:
        url = 'http://www.omdbapi.com/?apikey=<your-api-key-here>&i=' + imdb_id
        response = requests.get(url)
        data = response.json()

        # put into db
        genre_obj = []
        rating_obj = []

        genre_list = list(data['Genre'].replace(" ", "").split(','))

        for genre in genre_list:
            genre_slug = slugify(genre)
            g, created = Genre.objects.get_or_create(title=genre, slug=genre_slug)
            genre_obj.append(g)

        for rate in data['Ratings']:
            r, created = Rating.objects.get_or_create(source=rate['Source'], rated=rate['Value'])
            rating_obj.append(r)

        if data['Type'] == 'movie':
            m, created = MovieSeries.objects.get_or_create(
                Title = data["Title"],
                Year = data["Year"],
                Plot = data["Plot"],
                Lang = data["Language"],
                Poster_url = data['Poster'],
                Type = data["Type"],
                imdbRating = data["imdbRating"],
                imdbID = data["imdbID"],
            )
            m.Genre.set(genre_obj)
            m.Ratings.set(rating_obj)

        else:
            m, created = MovieSeries.objects.get_or_create(
                Title = data["Title"],
                Year = data["Year"],
                Plot = data["Plot"],
                Lang = data["Language"],
                Poster_url = data['Poster'],
                Type = data["Type"],
                Seasons = data["totalSeasons"],
                imdbRating = data["imdbRating"],
                imdbID = data["imdbID"],
            )
            m.Genre.set(genre_obj)
            m.Ratings.set(rating_obj)

        in_db = False

    if request.method == 'POST':
        user = request.user
        imdbid = request.POST.get('imdbID')
        watch = MovieSeries.objects.get(imdbID=imdbid)
        watchList = Watchlist(user=user,watchlist=watch)
        watchList.save()
        return redirect('watchlist')


    context = {
        'data': data,
        'in_db': in_db,
    }

    return render(request, 'desc.html', context)

@login_required
def watchlist(request):
    user = request.user
    data = Watchlist.objects.filter(user=user)
    context={
        'data' : data
    }
    return render(request, 'watchlist.html', context)

def profile(request):
    return render(request, 'profile.html', context={})

def movies(request):
    info = MovieSeries.objects.all()
    context = {
        'info': info
    }
    return render(request, 'movies.html', context)

def shows(request):
    info = MovieSeries.objects.all()
    context = {
        'info': info
    }
    return render(request, 'shows.html', context)
