from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from users.serializers import UserModelSerializer
from .serializers import UserRegisterationSerializer
from rest_framework.response import Response
from rest_framework import status
from knox.auth import AuthToken
from users.models import User


class Register(ObtainAuthToken):
    def post(self, request):
        serializer = UserRegisterationSerializer(data = request.data)
        if serializer.is_valid():
            user_serializer = UserModelSerializer(data = serializer.data)
            if user_serializer.is_valid():
                username = serializer.validated_data['username']
                email = serializer.validated_data['email']
                password = serializer.validated_data['password1']
                user = User.objects.create_user(username=username, email=email, password=password)
                _, token = AuthToken.objects.create(user)
                return Response({
                    "token" : token,
                    "user" : {
                        "id" : user.id,
                        "username" : user.username
                    }
                })

            return Response(user_serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



class Login(ObtainAuthToken):
    auth_serializer = AuthTokenSerializer

    def get(self, request):
        serializer = AuthTokenSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            _, token = AuthToken.objects.create(user)
            return Response({
                "token" : token,
                "user" : {
                    "id" : user.id,
                    "username" : user.username,
                    "email" : user.email,
                    "bio" : user.bio
                }
            })
        return Response(serializer.errors, status.HTTP_401_UNAUTHORIZED)


