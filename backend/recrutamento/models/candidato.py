from crum import get_current_user
from django.db import models
from emails.models.mensagem_email import MensagemEmail
from emails.models.template_email import TemplateEmail

from .vaga import Vaga


class Candidato(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )

    vaga = models.ForeignKey(
        Vaga,
        verbose_name="Vaga",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    sobre_mim = models.TextField(verbose_name="Sobre Mim")

    email = models.EmailField(
        verbose_name="E-mail",
        max_length=100,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
        null=True,
        blank=True,
        help_text="Apenas números, sem pontos ou traços.",
    )
    
    whatsapp = models.CharField(
        verbose_name="WhatsApp",
        max_length=20,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        null=True,
    )

    ESTADO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )

    estado = models.CharField(
        verbose_name="Estado", max_length=2, choices=ESTADO_CHOICES
    )

    expectativa_2anos = models.TextField(
        verbose_name="Expectativa para os próximos 2 anos"
    )

    expectativa_10anos = models.TextField(
        verbose_name="Expectativa para os próximos 10 anos"
    )

    comunicativo = models.BooleanField(verbose_name="Comunicativo", default=False)

    INGLES_CHOICES = (
        (0, "Não tem"),
        (1, "Básico"),
        (2, "Intermediário"),
        (3, "Avançado"),
        (4, "Fluente"),
    )

    ingles = models.IntegerField(
        verbose_name="Inglês", choices=INGLES_CHOICES, default=0
    )

    empregado = models.BooleanField(verbose_name="Empregado", default=False)

    DISPONIBILIDADE_CHOICES = (
        ("IMEDIATA", "Imediata"),
        ("30DIAS", "30 dias"),
        ("60DIAS", "60 dias"),
        ("90DIAS", "90 dias"),
        ("120DIAS", "120 dias"),
    )

    disponibilidade = models.CharField(
        verbose_name="Disponibilidade",
        max_length=8,
        choices=DISPONIBILIDADE_CHOICES,
        default="IMEDIATA",
    )

    HORARIOS_CHOICES = (
        ("PART-TIME", "Part-time"),
        ("FULL-TIME", "Full-time"),
    )

    horarios = models.CharField(
        verbose_name="Horários",
        max_length=9,
        choices=HORARIOS_CHOICES,
        default="FULL-TIME",
    )

    pretensao_salarial_pj = models.DecimalField(
        verbose_name="Pretensão Salarial PJ",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    pretensao_salarial_clt = models.DecimalField(
        verbose_name="Pretensão Salarial CLT",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    curriculo = models.FileField(
        verbose_name="Currículo",
        upload_to="curriculos",
        blank=False,
        null=False,
    )

    github_portfolio = models.URLField(
        verbose_name="GitHub/Porfolio",
        blank=True,
        null=True,
    )

    linkedin = models.URLField(
        verbose_name="Linkedin",
        blank=True,
        null=True,
    )

    indicacao = models.TextField(
        verbose_name="Indicação",
        blank=True,
        null=True,
    )

    teste_tecnico = models.FileField(
        verbose_name="Teste Técnico",
        upload_to="testes_tecnicos/",
        blank=True,
        null=True,
    )
    
    link_teste_tecnico = models.URLField(
        verbose_name="Link do Teste Técnico",
        blank=True,
        null=True,
    )

    resposta_vaga_generica = models.TextField(
        verbose_name="Para qual cargo e nível você gostaria de se candidatar?",
        blank=True,
        null=True,
        help_text="Ex: Analista de Dados Pleno"
    )

    interesse_diferenciais = models.TextField(
        verbose_name="Interesse ou contato com os diferenciais",
        help_text="Explique brevemente seu interesse ou contato com os diferenciais escolhidos.",
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


    def notificar_usuario_nova_candidatura(self):
 
        
        try:
            
            template_email = TemplateEmail.objects.get(codigo='confirmar_candidatura')

            mensagem_email = MensagemEmail.objects.create(template_email=template_email)
            
            destinatarios_extra = []

            if self.email: 
                destinatarios_extra.append(self.email)
            mensagem_email.enviar(self, destinatarios_extra)
        except Exception as e:
            print("Erro ao enviar email:", str(e))
            
            
    def __str__(self):
        """Método que retorna a representação do objeto como string."""
        return self.nome

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None

        if not self.pk:
            self.usuario_criacao = user

        self.usuario_atualizacao = user
        super(Candidato, self).save(*args, **kwargs)

    class Meta:
        """Sub classe para definir meta atributos da classe principal."""

        app_label = "recrutamento"
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"
        constraints = [
            models.UniqueConstraint(fields=["email", "vaga"], name="unique_email_vaga"),
        ]