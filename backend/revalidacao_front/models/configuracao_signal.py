from django.db import models
from crum import get_current_user
from django.contrib.contenttypes.models import ContentType
from .configuracao_webhook import ConfiguracaoWebhook


class ConfiguracaoSignal(models.Model):
    configuracao_webhook = models.ForeignKey(
        ConfiguracaoWebhook, on_delete=models.CASCADE
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    ativa = models.BooleanField(
        verbose_name="Ativa",
        default=True,
    )

    create = models.BooleanField(
        verbose_name="Create",
        default=True,
    )

    update = models.BooleanField(
        verbose_name="Update",
        default=True,
    )

    delete = models.BooleanField(
        verbose_name="Delete",
        default=True,
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação", auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name="Data de Atualização", auto_now=True
    )

    usuario_criacao = models.ForeignKey(
        "auth.User",
        related_name="%(class)s_requests_created",
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
    )

    usuario_atualizacao = models.ForeignKey(
        "auth.User",
        related_name="%(class)s_requests_modified",
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return f"{self.configuracao_webhook} - {self.content_type}"

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None

        if not self.pk:
            self.usuario_criacao = user

        self.usuario_atualizacao = user
        super(ConfiguracaoSignal, self).save(*args, **kwargs)

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "revalidacao_front"
        verbose_name = "Configuração de Signal"
        verbose_name_plural = "Configurações de Signal"
