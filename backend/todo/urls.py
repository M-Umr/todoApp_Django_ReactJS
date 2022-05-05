from .views import TodoView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('todos',TodoView, 'todo')