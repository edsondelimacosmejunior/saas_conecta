from crum import get_current_user
from django.db import models
from .skill import Skill
from .vaga import Vaga

class PesoSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    PESO_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    ]

    peso = models.IntegerField(
        verbose_name="Peso",
        default=1,
        choices=PESO_CHOICES,
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
        return f'{self.id}'

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None

        if not self.pk:
            self.usuario_criacao = user

        self.usuario_atualizacao = user
        super(PesoSkill, self).save(*args, **kwargs)

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "recrutamento"
        verbose_name = "Peso Skill"
        verbose_name_plural = "Peso Skills"
