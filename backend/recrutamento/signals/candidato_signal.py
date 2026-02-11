from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Candidato


@receiver(post_save, sender=Candidato)
def candidato_post_save(sender, instance, created, **kwargs):
    '''Realiza ações após a model Candidato ser salva.'''
    if created:
        # instance.notificar_usuario_nova_candidatura()
        print(f'Novo candidato criado: {instance.nome}')
    else:
        print(f'Candidato atualizado: {instance.nome}')