import email, re
from rest_framework import serializers
from users.models import User

class UserRegisterationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate_email(self, data):
        print(data)
        if User.objects.filter(email=email):
            raise serializers.ValidationError("This email arleady exists")

        return email

    def validate_password1(self, password):
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            return password

        raise serializers.ValidationError("The password is weak!")

    def validate(self, data):
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError("The passwords don't match")
            
        return data

