from rest_framework import generic

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generic.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generic.RetreiveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
