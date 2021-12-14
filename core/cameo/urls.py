from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('cameo/<imdb_id>', views.description, name='desc'),
    path('profile/', views.profile, name='profile'),
]
