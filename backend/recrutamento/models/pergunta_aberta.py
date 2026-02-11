from crum import get_current_user
from django.db import models

from .vaga import Vaga


class PerguntaAberta(models.Model):
    titulo = models.CharField(
        verbose_name='Título',
        max_length=100,
    )

    vaga = models.ForeignKey(
        Vaga,
        verbose_name='Vaga',
        on_delete=models.CASCADE,
    )

    obrigatorio = models.BooleanField(
        verbose_name='Obrigatório',
        default=True,
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name="Data de Atualização",
        auto_now=True
    )

    usuario_criacao = models.ForeignKey(
        'auth.User', 
        related_name='%(class)s_requests_created',
        blank=True, null=True,
        default=None,
        on_delete=models.SET_NULL
    )
    
    usuario_atualizacao = models.ForeignKey(
        'auth.User', 
        related_name='%(class)s_requests_modified',
        blank=True, null=True,
        default=None,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.titulo
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None

        if not self.pk:
            self.usuario_criacao = user
        
        self.usuario_atualizacao = user
        super(PerguntaAberta, self).save(*args, **kwargs)

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'recrutamento'
        verbose_name = 'Pergunta Aberta'
        verbose_name_plural = 'Perguntas Abertas'
