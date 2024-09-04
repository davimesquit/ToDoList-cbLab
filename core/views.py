from django.shortcuts import render
from .models import Tarefa

def index(request):
    tarefas = Tarefa.objects.all()
    
    context = {
        'title': 'Django To-Do',
        'tarefas': tarefas,
    }
    return render(request, 'index.html', context)

def create(request):
    return render(request, 'create.html')

