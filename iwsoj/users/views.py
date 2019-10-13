# Create your views here.

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from users.serializers.user_serializer import UserSerializer


def register(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        serialized.create(serialized.validated_data)
        return HttpResponse(serialized.data, status=HTTP_201_CREATED)
    else:
        return HttpResponse(serialized.errors, status=HTTP_400_BAD_REQUEST)
