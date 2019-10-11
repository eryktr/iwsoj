from django.urls import path
from iwsoj.views import home
urlpatterns = [
    path("", home)
]
