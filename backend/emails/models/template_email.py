import logging

from django.db import models
from django_quill.fields import QuillField
from django.contrib.contenttypes.models import ContentType

from emails.models.configuracao_email import ConfiguracaoEmail

from .destinatario import Destinatario
from novadata_utils.models import AbstractNovadataModel
from tinymce.models import HTMLField
logger = logging.getLogger(__name__)


class TemplateEmail(AbstractNovadataModel):
    nome_interno = models.CharField(
        max_length=200,
        verbose_name="Nome interno do template",
        help_text="Nome interno do template, utilizado para identificar o template no sistema.",  # noqa: E501
        null=True,
    )

    codigo = models.CharField(
        max_length=50,
        verbose_name="Código",
        unique=True,
    )

    assunto = models.CharField(
        max_length=200,
        verbose_name="Assunto",
    )

    texto_acima_titulo = models.CharField(
        max_length=200,
        verbose_name="Texto acima do título",
        blank=True,
        null=True,
    )

    titulo_email = models.CharField(
        max_length=200,
        verbose_name="Título do email",
    )

    logo_superior = models.FileField(
        verbose_name="Logo superior",
        upload_to="emails/logos/",
        null=True,
    )

    titulo_alteracao_email = models.CharField(
        max_length=200,
        verbose_name="Título alteração do email",
        blank=True,
        null=True,
    )

    legenda_email = models.CharField(
        max_length=200,
        verbose_name="Legenda do email",
        blank=True,
        null=True,
    )

    tipo_objeto = models.ForeignKey(
        to=ContentType,
        verbose_name="Tipo de objeto",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Tipo de objeto relacionado ao template de email",
    )

    corpo_email = HTMLField(
        verbose_name="Corpo do email",
    )

    destinatarios = models.ManyToManyField(
        Destinatario,
        verbose_name="Destinatários",
        blank=True,
    )

    enviar_copia_oculta = models.ManyToManyField(
        Destinatario,
        verbose_name="Enviar cópia oculta",
        blank=True,
        related_name="destinatarios_copia_oculta",
    )

    primeiro_link = models.URLField(
        verbose_name="Primeiro link",
        blank=True,
        null=True,
    )

    texto_primeiro_link = models.CharField(
        max_length=200,
        verbose_name="Texto do primeiro link",
        blank=True,
        null=True,
    )

    segundo_link = models.URLField(
        verbose_name="Segundo link",
        blank=True,
        null=True,
    )

    texto_segundo_link = models.CharField(
        max_length=200,
        verbose_name="Texto do segundo link",
        blank=True,
        null=True,
    )

    enviar_usuario_criacao = models.BooleanField(
        verbose_name="Enviar usuário de criação",
    )

    ativo = models.BooleanField(
        verbose_name="Ativo",
        default=True,
    )

    responder_para = models.CharField(
        max_length=200,
        verbose_name="Responder para",
        blank=True,
        null=True,
    )

    smtp_especifico = models.ForeignKey(
        ConfiguracaoEmail,
        verbose_name="SMTP específico",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )


    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return str(self.nome_interno)

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "emails"
        verbose_name = "Template do email"
        verbose_name_plural = "Templates dos emails"
