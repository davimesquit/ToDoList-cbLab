from django.shortcuts import render
from .models import Tarefa
from django.contrib import messages
from .forms import TarefaModelForm
from django.shortcuts import redirect

def home(request):
    tarefas = Tarefa.objects.all()
    
    context = {
        'title': 'Django To-Do',
        'tarefas': tarefas,
    }
    return render(request, 'home.html', context)

def create(request):
    if str(request.method) == 'POST':
        form = TarefaModelForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            form = TarefaModelForm()
            return redirect('home')
        else: 
            messages.error(request, 'Erro ao cadastrar tarefa!')
    else: 
        form = TarefaModelForm()
        
    context = {
            'form': form,
    }
    return render (request, 'create.html',context)

def tarefa(request, pk):
    tarefaId = Tarefa.objects.get(id=pk)
    
    context = {
        'tarefa': tarefaId,
    }
    return render(request, 'tarefa.html', context)
