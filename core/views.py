from django.shortcuts import render
from .models import Tarefa
from django.contrib import messages
from .forms import TarefaModelForm
from .forms import TarefaCreateModelForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def home(request):
    tarefas = Tarefa.objects.all()
    
    ordenar_por = request.GET.get('ordenar', 'data')
    
    if ordenar_por == 'data':
        tarefas = tarefas.order_by('-dataCriacao')
    else:
        tarefas = tarefas.order_by('status')
    
    context = {
        'tarefas': tarefas,
        'ordenar_por': ordenar_por,
    }
    return render(request, 'home.html', context)

def create(request):
    if str(request.method) == 'POST':
        form = TarefaCreateModelForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            messages.success(request, 'Tarefa cadastrada com sucesso!')
            form = TarefaCreateModelForm()
            return redirect('home')
        else: 
            messages.error(request, 'Erro ao cadastrar tarefa!')
    else: 
        form = TarefaCreateModelForm()
        
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

def manage_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, id=pk)
    if request.method == 'POST':
        if 'edit' in request.POST:
            form = TarefaModelForm(request.POST, instance=tarefa)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                messages.error(request, 'Erro ao editar tarefa!')
        elif 'delete' in request.POST:
                tarefa.delete()
                return redirect('home')
    else:
        form = TarefaModelForm(instance=tarefa)
        print(form)
        
        context = {
            'form': form,
            'tarefa': tarefa,
        }
    
    return render(request, 'manage_tarefa.html', context)
