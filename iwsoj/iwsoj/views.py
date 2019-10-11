from django.http import HttpResponse


def home(request):
    return HttpResponse("Nothing to find here. Use the /api tree.", status=404)
