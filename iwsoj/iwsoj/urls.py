from django.urls import path, include
from users.api import CreateUserView
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path("", home),
    path("api/token_auth/", views.obtain_auth_token),
    path("api/tasks/", include("tasks.urls")),
    path("api/submissions/", include("submissions.urls")),
    path("api/register/", CreateUserView.as_view())
]
