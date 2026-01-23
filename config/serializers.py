from rest_framework import serializers
from django.contrib.auth import authenticate
from .tokens import get_tokens_for_user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    passwod = serializers.CharField(write_only=True)

    def validate(self,date):
        email = data.get("email")
        password = data.get("password")

        user = user.authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid Credentials")

        date["tokens"] = get_tokens_for_user(user)
        return data