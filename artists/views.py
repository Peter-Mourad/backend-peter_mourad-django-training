from django.shortcuts import render
from .models import Artist
from django.contrib.auth import authenticate, login
from artists.serializers import ArtistSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ArtistsList(APIView):
    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ArtistSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)