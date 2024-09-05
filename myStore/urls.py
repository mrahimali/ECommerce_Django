from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homePage'),
    path('signup/', SignUp, name='signup'),
    path('login/', Login, name='login'),
]
