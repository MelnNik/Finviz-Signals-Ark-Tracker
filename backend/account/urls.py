from django.conf.urls import url
from django.urls import path, include
from .models import RegisterApi
urlpatterns = [
      path('register', RegisterApi.as_view()),
]

#To login, make a post request to http://localhost:8000/api/token/