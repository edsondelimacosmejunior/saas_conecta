from django.apps import AppConfig


class RevalidacaoFrontConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "revalidacao_front"

    def ready(self):
        import revalidacao_front.signals
