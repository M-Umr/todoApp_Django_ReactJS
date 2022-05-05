from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', RegisterUser.as_view())
]


########################
from .views import TodoView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('todos',TodoView, 'todo')