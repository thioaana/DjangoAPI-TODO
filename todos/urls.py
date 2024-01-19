from django.urls import path, include

from .views import ListTodo, DetailTodo

urlpatterns = [
    path("<int:pk>/", DetailTodo_as_view()),
    path("", ListTodo_as_view()),
]
