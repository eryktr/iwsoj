from django.http import HttpResponse


def helloworld(request):
    return HttpResponse("Hello, world!", status=200)
