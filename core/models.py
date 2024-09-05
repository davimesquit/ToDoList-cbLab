from django.db import models

class Tarefa(models.Model):
    
    PENDENTE = 'P'
    CONCLUIDA = 'C'

    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (CONCLUIDA, 'Concluída'),
    ]
    
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.CharField('Descricao', max_length=300)
    status =  models.CharField(
        'Status',
        max_length=1,
        choices=STATUS_CHOICES,
        default=PENDENTE,
    )
    dataCriacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status, self.status)