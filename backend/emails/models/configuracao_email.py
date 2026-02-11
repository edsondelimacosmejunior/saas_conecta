from django.db import models
from django.contrib.auth.models import User


class ConfiguracaoEmail(models.Model):
    email_backend = models.CharField(
        verbose_name="EMAIL_BACKEND",
        max_length=100,
        default="django.core.mail.backends.smtp.EmailBackend",
    )

    email_use_tls = models.BooleanField(
        verbose_name="EMAIL_USE_TLS",
        default=True,
    )

    email_host = models.CharField(
        verbose_name="EMAIL_HOST",
        max_length=100,
        default="smtp.sendgrid.net",
    )

    email_port = models.IntegerField(
        verbose_name="EMAIL_PORT",
        default=2525,
    )

    email_host_user = models.CharField(
        verbose_name="EMAIL_HOST_USER",
        max_length=100,
        default="apikey",
    )

    email_host_password = models.CharField(
        verbose_name="EMAIL_HOST_PASSWORD",
        max_length=100,
        default="",  # Configure via Django Admin
    )

    default_from_email = models.CharField(
        verbose_name="DEFAULT_FROM_EMAIL",
        max_length=100,
        default="Novadata <hub@novadata.com.br>",
    )

    email_name = models.CharField(
        verbose_name="EMAIL_NAME",
        max_length=100,
        default="Novadata",
    )

    email_timeout = models.IntegerField(
        verbose_name="EMAIL_TIMEOUT",
        default=30,
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )
    
    data_atualizacao = models.DateTimeField(
        verbose_name='Data de atualização',
        auto_now=True
    )

    usuario_criacao = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Usuário de criação',
        blank=True,
        null=True,
    )
    
    usuario_atualizacao = models.ForeignKey(
        User,
        related_name='%(class)s_requests_modified',
        verbose_name='Usuário de atualização',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    def save(self, *args, **kwargs):
        '''Sobrescrita do método save para realizarmos ações personalizadas.'''
        from crum import get_current_user
    
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user

        super(ConfiguracaoEmail, self).save(*args, **kwargs)

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return f"{self.email_name} - {self.email_host_user}"

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "emails"
        verbose_name = "Configuração de e-mail"
        verbose_name_plural = "Configurações de e-mail"