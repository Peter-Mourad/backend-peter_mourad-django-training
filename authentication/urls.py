from urllib.parse import urlparse
from django.urls import path
from knox import views as knox_views

from . import views

urlpatterns = [
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/',  knox_views.LogoutView.as_view()),
]