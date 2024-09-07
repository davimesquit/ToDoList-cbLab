from django import forms
from .models import Tarefa

class TarefaCreateModelForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao',]

class TarefaModelForm(forms.ModelForm):
        class Meta:
            model = Tarefa
            fields = ['titulo', 'descricao', 'status']

