from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserModelSerializer
from rest_framework import permissions

class IsTheCurrentUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

