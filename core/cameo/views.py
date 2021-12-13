from django.http import response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests


def index(request):
    query = request.GET.get('q')
    if query:
        url = 'http://www.omdbapi.com/?apikey=64830d56&s=' + query
        response = requests.get(url)
        data = response.json()
        context = {
            'query' : query,
            'data' : data,
        }
        return render(request, 'results.html', context)      
    return render(request, 'index.html', context={})

def register(request):
    return render(request, 'register.html', context={})

def login(request):
    return render(request, 'login.html', context={})

@login_required
def watchlist(request):
    return render(request, 'watchlist.html', context={})

def description(request):
    return render(request, 'desc.html', context={})

def profile(request):
    return render(request, 'profile.html', context={})