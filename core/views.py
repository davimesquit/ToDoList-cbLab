from django.shortcuts import render
from django.shortcuts import get_object_or_404
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
    tarefaId = Tarefa.objects.get(id=pk)
    
    context = {
        'tarefa': tarefaId,
    }
    return render(request, 'tarefa.html', context)
