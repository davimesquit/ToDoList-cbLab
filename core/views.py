from django.shortcuts import render
from .models import Tarefa
from django.contrib import messages
from .forms import TarefaModelForm
from .forms import TarefaCreateModelForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q, Case, When, Value, IntegerField
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    tarefas = Tarefa.objects.all()
    
    query = request.GET.get('query', '')
    ordenar_por = request.GET.get('ordenar', 'data')
    
    if query:
        tarefas = tarefas.filter(
            Q(titulo__icontains=query) | Q(descricao__icontains=query)
        )
    
    if ordenar_por == 'status':
        tarefas = tarefas.order_by(
            Case(
                When(status='P', then=Value(0)),
                default=Value(1),
                output_field=IntegerField(),
            ),
            '-dataCriacao'
        )
    else:
        tarefas = tarefas.order_by('-dataCriacao')
    
    paginator = Paginator(tarefas, 10)  # Mostra 10 tarefas por página
    page = request.GET.get('page')

    try:
        tarefas_pag = paginator.page(page)
    except PageNotAnInteger:
        tarefas_pag = paginator.page(1)
    
    context = {
        'tarefasPg': tarefas_pag,
        'ordenar_por': ordenar_por,
        'query': query,
    }
    return render(request, 'home.html', context)

def create(request):
    if str(request.method) == 'POST':
        form = TarefaCreateModelForm(request.POST)
        if form.is_valid():
            
            form.save()
            
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
