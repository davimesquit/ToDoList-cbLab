from django.urls import path
from .views import home, create, tarefa

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('tarefa/<int:pk>/', tarefa, name='tarefa'),
]
