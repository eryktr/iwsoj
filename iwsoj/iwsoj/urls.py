from django.urls import path
from iwsoj.views import helloworld
urlpatterns = [
    path("", helloworld)
]
