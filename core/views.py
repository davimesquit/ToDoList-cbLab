from django.shortcuts import render
from .models import Tarefa

def home(request):
    tarefas = Tarefa.objects.all()
    
    context = {
        'title': 'Django To-Do',
        'tarefas': tarefas,
    }
    return render(request, 'home.html', context)

def create(request):
    return render(request, 'create.html')

def tarefa(request, pk):
    print(f'PK: {pk}')
    tarefaId = Tarefa.objects.get(id=pk)
    context = {
        'tarefa': tarefaId,
    }
    return render(request, 'tarefa.html', context)

