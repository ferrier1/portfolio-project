from django.urls import path, include
from django.conf import settings
from . import views



urlpatterns = [
    path('', views.allblogs, name='home')
]
