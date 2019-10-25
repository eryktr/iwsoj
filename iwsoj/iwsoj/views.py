from django.http import HttpResponse
from rest_framework.status import HTTP_404_NOT_FOUND


def home(request):
    return HttpResponse("Nothing to find here. Use the /api tree.", status=HTTP_404_NOT_FOUND)
