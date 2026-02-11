from crum import get_current_user
from django.db import models

from .candidato import Candidato
from .pergunta_aberta import PerguntaAberta


class RespostaAberta(models.Model):
    candidato = models.ForeignKey(
        Candidato,
        verbose_name='Candidato',
        on_delete=models.CASCADE,
    )

    pergunta_aberta = models.ForeignKey(
        PerguntaAberta,
        verbose_name='Pergunta',
        on_delete=models.CASCADE,
    )

    resposta = models.TextField(
        verbose_name='Resposta',
        blank=True,
        null=True,
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
        return f"{self.candidato} - {self.pergunta_aberta}"
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None

        if not self.pk:
            self.usuario_criacao = user
        
        self.usuario_atualizacao = user
        super(RespostaAberta, self).save(*args, **kwargs)

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'recrutamento'
        verbose_name = 'Resposta Aberta'
        verbose_name_plural = 'Respostas Abertas'
