from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('gamemodes/', views.gamemodes, name='gamemodes'),
    path('ranking/', views.ranking, name='ranking'),
    path('servers/', views.servers, name='servers'),
    path('tutorials/', views.tutorials, name='tutorials'),
]