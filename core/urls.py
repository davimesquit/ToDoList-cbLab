from django.urls import path
from .views import home, create, manage_tarefa

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('manage_tarefa/<int:pk>/', manage_tarefa, name='manage_tarefa'),
]