from django.http import HttpResponse
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.status import HTTP_201_CREATED


def home(request):
    return HttpResponse("Nothing to find here. Use the /api tree.", status=HTTP_404_NOT_FOUND)


def index(request):
    return HttpResponse("Index page was created.", status=HTTP_201_CREATED)


def login(request):
    return HttpResponse("Login page was created.", status=HTTP_201_CREATED)


def register(request):
    return HttpResponse("Register page was created.", status=HTTP_201_CREATED)
