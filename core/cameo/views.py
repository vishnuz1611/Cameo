from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse
# Create your views here.

def index(request):
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