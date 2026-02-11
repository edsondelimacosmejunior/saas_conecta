from crum import get_current_user
from django.db import models
from django_editorjs import EditorJsField


class Vaga(models.Model):
    titulo = models.CharField(
        verbose_name='Título',
        max_length=100,
    )

    slug = models.SlugField(
        verbose_name='Slug',
        max_length=100,
        unique=True,
    )

    sobre = EditorJsField(
        verbose_name='Sobre a Vaga',
        blank=True,
        null=True,
    )

    ativa = models.BooleanField(
        verbose_name='Ativa',
        default=True,
    )

    responsabilidades = EditorJsField(
        verbose_name='Responsabilidades',
        blank=True,
        null=True,
    )

    data_fechamento = models.DateField(
        verbose_name='Data de Fechamento',
        blank=True,
        null=True,
    )

    salario = models.CharField(
        verbose_name='Salário',
        max_length=100,
        blank=True,
        null=True,
    )

    TIPO_CONTRATACAO_CHOICES = (
        ('CLT', 'CLT'),
        ('PJ', 'PJ'),
        ('ESTAGIO', 'Estágio'),
        ('FREELANCER', 'Freelancer'),
    )

    tipo_contratacao = models.CharField(
        verbose_name='Tipo de Contratação',
        max_length=10,
        choices=TIPO_CONTRATACAO_CHOICES,
        default='CLT',
    )

    vaga_generica = models.BooleanField(
        default=False,
        verbose_name="Vaga genérica",
        help_text="Marque se esta vaga for genérica"
    )

    TIPO_REGIME_TRABALHO_CHOICES = (
        ('PRESENCIAL', 'Presencial'),
        ('HIBRIDO', 'Híbrido'),
        ('HOME_OFFICE', 'Home Office'),
    )

    tipo_regime_trabalho = models.CharField(
        verbose_name='Tipo de Regime de Trabalho',
        max_length=20,
        choices=TIPO_REGIME_TRABALHO_CHOICES,
        default='PRESENCIAL',
    )

    area_atuacao = models.ForeignKey(
        'AreaAtuacao',
        verbose_name='Área de Atuação',
        on_delete=models.SET_NULL,
        null=True,
    )

    beneficios = models.ManyToManyField(
        'Beneficio',
        verbose_name='Benefícios',
        blank=True,
    )

    requisitos = models.ManyToManyField(
        'Skill',
        verbose_name='Requisitos',
        related_name='vaga_requisitos',
        blank=True,
    )

    diferenciais = models.ManyToManyField(
        'Skill',
        verbose_name='Diferenciais',
        related_name='vaga_diferenciais',
        blank=True,
    )

    teste_tecnico = models.FileField(
        verbose_name="Teste Técnico",
        upload_to="testes_tecnicos/",
        blank=True,
        null=True
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
        return self.titulo
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None

        if not self.pk:
            self.usuario_criacao = user
        
        self.usuario_atualizacao = user
        super(Vaga, self).save(*args, **kwargs)

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'recrutamento'
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
