import email
from rest_framework import serializers
from users.models import User

class UserRegisterationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError("The passwords don't match")
        return data

    def validate_email(self, email):
        if User.objects.filter(email=email):
            raise serializers.ValidationError("This email arleady exists")
        return email

