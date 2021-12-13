from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('description/', views.description, name='desc'),
    path('profile/', views.profile, name='profile'),
]
