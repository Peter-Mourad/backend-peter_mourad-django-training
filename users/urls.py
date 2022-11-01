from urllib.parse import urlparse
from django.urls import path

from . import views

user = views.UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update'
})

urlpatterns = [
    path('<int:pk>', user)
]