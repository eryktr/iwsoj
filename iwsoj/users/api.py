from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication
from .serializers.user_serializer import UserSerializer


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class AuthUserToken(TokenAuthentication):
    keyword = "Bearer"

