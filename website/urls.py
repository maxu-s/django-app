from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('download/', views.download, name='download'),
    path('servers/', views.servers, name='servers'),
    path('tutorials/', views.tutorials, name='tutorials'),
]
