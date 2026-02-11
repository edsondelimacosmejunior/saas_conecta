from crum import get_current_user
from django.db import models

from .candidato import Candidato
from .curso import Curso
from .instituicao import Instituicao


class FormacaoCandidato(models.Model):
    candidato = models.ForeignKey(
        Candidato,
        verbose_name="Candidato",
        on_delete=models.CASCADE,
    )

    instituicao = models.ForeignKey(
        Instituicao,
        verbose_name="Instituição",
        on_delete=models.CASCADE,
    )

    curso = models.ForeignKey(
        Curso,
        verbose_name="Curso",
        on_delete=models.CASCADE,
    )

    GRAU_CHOICES = (
        (1, "Técnico Incompleto"),
        (2, "Técnico"),
        (3, "Graduação Incompleta"),
        (4, "Graduação"),
        (5, "Pós-Graduação Incompleta"),
        (6, "Pós-Graduação"),
        (7, "Mestrado Incompleto"),
        (8, "Mestrado"),
        (9, "Doutorado Incompleto"),
        (10, "Doutorado"),
    )

    grau = models.IntegerField(
        verbose_name="Grau",
        choices=GRAU_CHOICES,
        default=1,
    )

    data_inicio = models.DateField(
        verbose_name="Data de Início",
    )

    data_conclusao = models.DateField(
        verbose_name="Data de Conclusão",
        blank=True,
        null=True,
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
        return f"{self.candidato} - {self.instituicao} - {self.curso} - {self.grau}"

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None

        if not self.pk:
            self.usuario_criacao = user

        self.usuario_atualizacao = user
        super(FormacaoCandidato, self).save(*args, **kwargs)

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "recrutamento"
        verbose_name = "Benefício"
        verbose_name_plural = "Benefícios"
