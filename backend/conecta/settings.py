import os
from datetime import timedelta
from pathlib import Path

from decouple import Csv, config
from dj_database_url import parse as dburl
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY", "")

DEBUG = config("DEBUG", default=False, cast=bool)


# ALLOWED_HOSTS
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", cast=Csv())

INTERNAL_IPS = ["127.0.0.1", "localhost"]
CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=Csv())


INSTALLED_APPS = [
    "admin_reorder",
    "django_app_novadata",
    "django.contrib.admindocs",
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    #
    # Apps
    "avatar",
    "front_assets",
    "home",
    "recrutamento",
    "revalidacao_front",
    "emails",
    #
    # Libs
    # "advanced_filters",
    "corsheaders",
    "django_admin_listfilter_dropdown",
    "django_browser_reload",
    "django_object_actions",
    "django_filters",
    "django_editorjs",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "import_export",
    "novadata_utils",
    "rest_framework",
    "rest_framework.authtoken",
    "widget_tweaks",
    "debug_toolbar",
    "django_quill",
    "tinymce",

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "home.middlewares.ModelAndAppNameMiddleware",
    "admin_reorder.middleware.ModelAdminReorder",
    "crum.CurrentRequestUserMiddleware",
]

DEV = config("DEV", default=False, cast=bool)
if DEV:
    MIDDLEWARE += [
        "django_browser_reload.middleware.BrowserReloadMiddleware",
        # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = "conecta.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "conecta.wsgi.application"


default_dburl = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
DATABASES = {"default": config("DATABASE_URL", default=default_dburl, cast=dburl)}

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    #
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    #
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

SPECTACULAR_SETTINGS = {
    "TITLE": "conecta API",
    "DESCRIPTION": "conecta description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    #
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(weeks=1),
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa E501
    },
]

AUTHENTICATION_BACKENDS = [
    "global_functions.authentication.LoginUsernameEmail",
]


USE_POSTGRES = config("USE_POSTGRES", default=False, cast=bool)
if USE_POSTGRES:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": config("DATABASE_POSTGRES"),
            "USER": config("USER_POSTGRES"),
            "PASSWORD": config("PASSWORD_POSTGRES"),
            "HOST": config("HOST_POSTGRES"),
            "PORT": config("PORT_POSTGRES"),
            "OPTIONS": {
                "sslmode": "require",
            },
        }
    }
else:
    default_dburl = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    DATABASES = {"default": config("DATABASE_URL", default=default_dburl, cast=dburl)}


UNFOLD = {
    "SITE_TITLE": "Conecta Admin",
    "SITE_HEADER": "Administração - Conecta",
    "SITE_URL": "/",
    "COLORS": {
        "primary": {
            "50": "239 254 245",
            "100": "217 255 236",
            "200": "181 253 217",
            "300": "123 250 189",
            "400": "59 237 152",
            "500": "17 210 118",
            "600": "8 177 96",
            "700": "10 139 78",
            "800": "14 109 65",
            "900": "14 89 56",
            "950": "1 50 29",
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Recrutamento"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Áreas de Atuações"),
                        "icon": "hive",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy(
                            "admin:recrutamento_areaatuacao_changelist"
                        ),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Benefícios"),
                        "icon": "heart_plus",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:recrutamento_beneficio_changelist"),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Cursos"),
                        "icon": "school",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:recrutamento_curso_changelist"),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Candidato"),
                        "icon": "person_raised_hand",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:recrutamento_candidato_changelist"),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Instituições"),
                        "icon": "apartment",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy(
                            "admin:recrutamento_instituicao_changelist"
                        ),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Skills"),
                        "icon": "star_rate_half",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:recrutamento_skill_changelist"),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Vagas"),
                        "icon": "add_reaction",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:recrutamento_vaga_changelist"),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                ],
            },
            {
                "title": _("Sistema"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Grupos de Usuários"),
                        "icon": "groups",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:auth_group_changelist"),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": _("Tokens de Autenticação"),
                        "icon": "token",
                        "link": reverse_lazy("admin:authtoken_tokenproxy_changelist"),
                    },
                    {
                        "title": _("Configurações de Interface"),
                        "icon": "settop_component",
                        "link": reverse_lazy(
                            "admin:django_app_novadata_conteudocustom_changelist"
                        ),
                    },
                    {
                        "title": _("Configurações de Webhook de Front"),
                        "icon": "settop_component",
                        "link": reverse_lazy(
                            "admin:revalidacao_front_configuracaowebhook_changelist"
                        ),
                    },
                ],
            },
            {
                "title": _("Emails"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Mensagens de Email"),
                        "icon": "mail",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:emails_mensagememail_changelist"),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Templates de Email"),
                        "icon": "dynamic_feed",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:emails_templateemail_changelist"),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Destinatários"),
                        "icon": "contact_mail",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:emails_destinatario_changelist"),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": _("Configurações E-mail"),
                        "icon": "settop_component",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:emails_configuracaoemail_changelist"),
                        # "permission": lambda request: request.user.is_superuser,
                    },
                ],
            },
        ],
    },
}

ADMIN_REORDER = (
    {
        "app": "recrutamento",
        "label": "Recrutamento",
        "models": (
            {"model": "recrutamento.AreaAtuacao", "label": "Área de Atuação"},
            {"model": "recrutamento.Beneficio", "label": "Benefícios"},
            {"model": "recrutamento.Curso", "label": "Cursos"},
            {"model": "recrutamento.Candidato", "label": "Candidatos"},
            {"model": "recrutamento.Instituicao", "label": "Instituições"},
            {"model": "recrutamento.Skill", "label": "Skills"},
            {"model": "recrutamento.Vaga", "label": "Vagas"},
            {"model": "recrutamento.RespostaCandidatoSkillDiferencial", "label": "Resposta Candidato Skill Diferencial"},
        ),
    },
    {
        "app": "auth",
        "label": "Sistema",
        "models": (
            {"model": "auth.Group", "label": "Grupos de Usuários"},
            {"model": "auth.User", "label": "Usuários"},
            {"model": "authtoken.TokenProxy", "label": "Tokens de Autenticação"},
            {
                "model": "django_app_novadata.ConteudoCustom",
                "label": "Configurações de Interface",
            },
            {
                "model": "revalidacao_front.ConfiguracaoWebhook",
                "label": "Configurações de Webhook de Front",
            },
        ),
    },
    {
        "app": "emails",
        "label": "E-mails",
        "models": (
            "emails.MensagemEmail",
            "emails.TemplateEmail",
            "emails.Destinatario",
            "emails.ConfiguracaoEmail"
        ),
    },
)

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
LOCALHOST_URL = "http://localhost:8000"


STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

USE_AWS = config("USE_AWS", default=False, cast=bool)
if USE_AWS:
    """
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "access_key": config("AWS_ACCESS_KEY_ID"),
                "secret_key": config("AWS_SECRET_ACCESS_KEY"),
                "bucket_name": config("AWS_NAME_BUCKET"),
                "default_acl": None,
                "location": "static",
                "custom_domain": config("LINK_CLOUD"),
                "object_parameters": {
                    "CacheControl": "max-age=86400",
                },
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "access_key": config("AWS_ACCESS_KEY_ID"),
                "secret_key": config("AWS_SECRET_ACCESS_KEY"),
                "bucket_name": config("AWS_NAME_BUCKET"),
                "default_acl": None,
                "location": "static",  # Arquivos estáticos
                "custom_domain": config("LINK_CLOUD"),
                "object_parameters": {
                    "CacheControl": "max-age=86400",
                },
            },
        },
        "media": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "access_key": config("AWS_ACCESS_KEY_ID"),
                "secret_key": config("AWS_SECRET_ACCESS_KEY"),
                "bucket_name": config("AWS_NAME_BUCKET"),
                "default_acl": None,
                "location": "media",  # Diretório correto para os uploads
                "custom_domain": config("LINK_CLOUD"),
                "object_parameters": {
                    "CacheControl": "max-age=86400",
                },
            },
        },
    }

    # URLs para arquivos estáticos e mídia
    STATIC_URL = f"https://{config('AWS_NAME_BUCKET')}.s3.amazonaws.com/static/"
    MEDIA_URL = f"https://{config('AWS_NAME_BUCKET')}.s3.amazonaws.com/media/"

    DEFAULT_FILE_STORAGE = 'conecta.storage_backends.PublicMediaStorage'
    FILE_UPLOAD_TEMP_STORAGE = 'conecta.storage_backends.TemporaryMediaStorage'
    """
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = config("AWS_NAME_BUCKET")
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }
    AWS_LOCATION = "static"
    AWS_DEFAULT_ACL = None

    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)
    DEFAULT_FILE_STORAGE = "conecta.storage_backends.PublicMediaStorage"
