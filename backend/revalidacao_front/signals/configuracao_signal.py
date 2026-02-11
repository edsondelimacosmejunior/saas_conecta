from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from ..models import ConfiguracaoSignal


def notificar_front(instance, **kwargs):
    """Algoritmo executado pelos signals"""
    print(f"Executando algoritmo X para {instance}")


def registrar_signals():
    """Registra os signals dinamicamente com base nas configurações"""
    for signal_config in ConfiguracaoSignal.objects.filter(ativa=True):
        model_class = signal_config.content_type.model_class()

        if signal_config.create:
            post_save.connect(
                notificar_front,
                sender=model_class,
                weak=False,
                dispatch_uid=f"{model_class}_front_revalidate_create",
            )

        if signal_config.update:
            pre_save.connect(
                notificar_front,
                sender=model_class,
                weak=False,
                dispatch_uid=f"{model_class}_front_revalidate_update",
            )

        if signal_config.delete:
            post_delete.connect(
                notificar_front,
                sender=model_class,
                weak=False,
                dispatch_uid=f"{model_class}_front_revalidate_delete",
            )


def desconectar_signals():
    """Desconecta todos os signals registrados dinamicamente"""
    for signal_config in ConfiguracaoSignal.objects.filter(ativa=True):
        model_class = signal_config.content_type.model_class()

        post_save.disconnect(
            notificar_front,
            sender=model_class,
            dispatch_uid=f"{model_class}_front_revalidate_create",
        )
        pre_save.disconnect(
            notificar_front,
            sender=model_class,
            dispatch_uid=f"{model_class}_front_revalidate_update",
        )
        post_delete.disconnect(
            notificar_front,
            sender=model_class,
            dispatch_uid=f"{model_class}_front_revalidate_delete",
        )


# Listener para alterações em ConfiguracaoSignal
@receiver(post_save, sender=ConfiguracaoSignal)
def atualizar_signals(sender, instance, **kwargs):
    """Atualiza os signals dinamicamente sempre que ConfiguracaoSignal for alterado"""
    print("Atualizando signals")
    desconectar_signals()
    registrar_signals()


@receiver(post_delete, sender=ConfiguracaoSignal)
def atualizar_signals_delete(sender, instance, **kwargs):
    """Atualiza os signals dinamicamente sempre que ConfiguracaoSignal for excluído"""
    print("Atualizando signals")
    desconectar_signals()
    registrar_signals()
