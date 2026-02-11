from crum import get_current_user
from django.db import models

from .candidato import Candidato
from .skill import Skill


class SkillCandidato(models.Model):
    candidato = models.ForeignKey(
        Candidato,
        verbose_name='Candidato',
        on_delete=models.CASCADE,
    )

    skill = models.ForeignKey(
        Skill,
        verbose_name='Skill',
        on_delete=models.CASCADE,
    )

    AVALIACAO_CHOICES = (
        (0, 'Não Possui'),
        (1, 'Básico'),
        (2, 'Intermediário'),
        (3, 'Avançado'),
        (4, 'Especialista'),
    )

    avaliacao = models.IntegerField(
        verbose_name='Avaliação',
        choices=AVALIACAO_CHOICES,
        default=0,
    )

    TEMPO_EXPERIENCIA_CHOICES = (
        (0, 'Não Possui'),
        (1, 'Mais de 1 ano'),
        (2, 'Mais de 2 anos'),
        (3, 'Mais de 3 anos'),
        (4, 'Mais de 4 anos'),
        (5, 'Mais de 5 anos'),
        (6, 'Mais de 6 anos'),
        (7, 'Mais de 7 anos'),
        (8, 'Mais de 8 anos'),
        (9, 'Mais de 9 anos'),
        (10, 'Mais de 10 anos'),
    )

    tempo_experiencia = models.IntegerField(
        verbose_name='Tempo de Experiência',
        choices=TEMPO_EXPERIENCIA_CHOICES,
        default=0,
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
        return f"{self.candidato} - {self.skill}"
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None

        if not self.pk:
            self.usuario_criacao = user
        
        self.usuario_atualizacao = user
        super(SkillCandidato, self).save(*args, **kwargs)

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'recrutamento'
        verbose_name = 'Skill do Candidato'
        verbose_name_plural = 'Skills dos Candidatos'
