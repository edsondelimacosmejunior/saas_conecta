from django.db import models
from novadata_utils.models import AbstractNovadataModel

from emails.models.template_email import TemplateEmail



class AnexoEmail(AbstractNovadataModel):
    nome_interno = models.CharField(
        max_length=200,
        verbose_name="Nome interno do anexo",
        help_text="Nome interno do anexo, utilizado para identificar o anexo no sistema.",  # noqa: E501
    )

    anexo = models.FileField(
        verbose_name="Anexo",
        upload_to="emails/anexos/",
    )

    template_email = models.ForeignKey(
        to=TemplateEmail,
        verbose_name="Template de e-mail",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return str(self.nome_interno)

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "emails"
        verbose_name = "Anexo de e-mail"
        verbose_name_plural = "Anexos de e-mail"