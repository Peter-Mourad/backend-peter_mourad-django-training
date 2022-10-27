from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreateArtist.as_view()),
    path('', views.ArtistsHomePage.as_view()),
]