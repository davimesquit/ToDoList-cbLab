from django.test import TestCase
from model_mommy import mommy
from core.models import Tarefa

class TarefaModelTestCase(TestCase):
    
    def setUp(self):
        self.tarefa = mommy.make(Tarefa)
    
    def test_str(self):
        self.assertEqual(str(self.tarefa), self.tarefa.titulo)
    
    def test_get_status_display(self):
        self.assertEqual(self.tarefa.get_status_display(), 'Pendente')
