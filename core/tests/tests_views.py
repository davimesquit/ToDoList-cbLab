from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from core.models import Tarefa
from django.utils import timezone
from datetime import timedelta
from django.contrib.messages import get_messages

class homeViewTestCase(TestCase):

    def setUp(self):
        
        now = timezone.now()
        self.tarefa1 = Tarefa.objects.create(
            titulo='Tarefa 1',
            descricao='Descrição 1',
            status='C',
        )
        self.tarefa2 = Tarefa.objects.create(
            titulo='Tarefa 2',
            descricao='Descrição 2',
            status='C',
        )
        self.tarefa3 = Tarefa.objects.create(
            titulo='Tarefa 3',
            descricao='Descrição 3',
            status='P',
        )
        
        self.tarefa1.dataCriacao = now - timedelta(days=2)
        self.tarefa1.save()
        
        self.tarefa2.dataCriacao = now - timedelta(days=1)
        self.tarefa2.save()
        
        self.tarefa3.dataCriacao = now
        self.tarefa3.save()

    def test_home_view_status_code(self):
        """Teste para verificar se a view retorna uma resposta 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_query_filter(self):
        """Testa o filtro da busca por query"""
        response = self.client.get(reverse('home') + '?query=Tarefa 1')
        self.assertContains(response, "Tarefa 1")
        self.assertNotContains(response, "Tarefa 2")

    def test_home_view_order_by_status(self):
        """Testa se a ordenação por status está funcionando"""
        response = self.client.get(reverse('home') + '?ordenar=status')
        tarefas_ordenadas = response.context['tarefasPg'].object_list
        
        self.assertEqual(tarefas_ordenadas[0].titulo, "Tarefa 3")  
        
    def test_home_view_order_by_data(self):
        """Testa se a ordenação por data está funcionando"""
        response = self.client.get(reverse('home') + '?ordenar=data')
        tarefas_ordenadas = response.context['tarefasPg'].object_list
        
        self.assertEqual(tarefas_ordenadas[0].titulo, 'Tarefa 3')
        self.assertEqual(tarefas_ordenadas[1].titulo, 'Tarefa 2')
        self.assertEqual(tarefas_ordenadas[2].titulo, 'Tarefa 1') 
        

    def test_home_view_pagination(self):
        """Testa se a paginação está funcionando"""
        for i in range(12):
            Tarefa.objects.create(titulo=f"Tarefa {i + 4}", descricao=f"Descrição da tarefa {i + 4}", status='P')

        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['tarefasPg']), 10)

        response = self.client.get(reverse('home') + '?page=2')
        self.assertEqual(len(response.context['tarefasPg']), 5) 
        
class CreateViewTestCase(TestCase):

    def setUp(self):
        pass

    def test_create_view_get(self):
        """Testa se o formulário de criação é exibido corretamente via GET."""
        response = self.client.get(reverse('create'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')
        self.assertIn('form', response.context)

    def test_create_view_post_valid(self):
        """Testa se uma tarefa válida é criada com sucesso via POST."""
        
        data = {
            'titulo': 'Nova Tarefa',
            'descricao': 'Descrição da nova tarefa',
        }
        response = self.client.post(reverse('create'), data)
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        
        self.assertTrue(Tarefa.objects.filter(titulo='Nova Tarefa').exists())

    def test_create_view_post_invalid(self):
        """Testa se uma tarefa inválida não é criada e uma mensagem de erro é exibida."""

        data = {
            'titulo': '',
            'descricao': 'Descrição inválida',
        }
        response = self.client.post(reverse('create'), data)
        
        self.assertEqual(response.status_code, 200)
        
        self.assertFalse(Tarefa.objects.filter(descricao='Descrição inválida').exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Erro ao cadastrar tarefa!')

class ManageTarefaViewTestCase(TestCase):

    def setUp(self):
        self.tarefa = Tarefa.objects.create(
            titulo='Tarefa de Teste',
            descricao='Descrição de teste',
        )

    def test_manage_tarefa_view_get(self):
        """Testa se o formulário com os dados da tarefa é exibido corretamente via GET."""
        response = self.client.get(reverse('manage_tarefa', kwargs={'pk': self.tarefa.pk}))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manage_tarefa.html')
        self.assertIn('form', response.context)  
        self.assertIn('tarefa', response.context)  
        self.assertEqual(response.context['tarefa'], self.tarefa)  

    def test_manage_tarefa_view_post_edit_valid(self):
        """Testa se a tarefa é editada corretamente ao submeter dados válidos via POST."""
        data = {
            'titulo': 'Tarefa Editada',
            'descricao': 'Descrição editada',
            'status': 'C'
        }
        response = self.client.post(reverse('manage_tarefa', kwargs={'pk': self.tarefa.pk}), data={'edit': True, **data})
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        
        self.tarefa.refresh_from_db()
        self.assertEqual(self.tarefa.titulo, 'Tarefa Editada')
        self.assertEqual(self.tarefa.descricao, 'Descrição editada')
        self.assertEqual(self.tarefa.status, 'C')

    def test_manage_tarefa_view_post_edit_invalid(self):
        """Testa se a tarefa não é editada ao submeter dados inválidos e uma mensagem de erro é exibida."""
        data = {
            'titulo': '', 
            'descricao': 'Descrição com erro',
        }
        response = self.client.post(reverse('manage_tarefa', kwargs={'pk': self.tarefa.pk}), data={'edit': True, **data})
        
        self.assertEqual(response.status_code, 200)
        
        self.tarefa.refresh_from_db()
        self.assertNotEqual(self.tarefa.descricao, 'Descrição com erro')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Erro ao editar tarefa!')

    def test_manage_tarefa_view_post_delete(self):
        """Testa se a tarefa é deletada corretamente ao submeter a requisição de deletar via POST."""
        response = self.client.post(reverse('manage_tarefa', kwargs={'pk': self.tarefa.pk}), data={'delete': True})
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        
        self.assertFalse(Tarefa.objects.filter(pk=self.tarefa.pk).exists())
