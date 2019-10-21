from django.urls import path

from iwsoj.views import home
from iwsoj.views import index
from iwsoj.views import login
from iwsoj.views import register

urlpatterns = [
    path("", home),
    path("index.html", index),
    path("login.html", login),
    path("register.html", register)

]
