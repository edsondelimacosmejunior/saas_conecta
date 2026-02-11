from django.apps import AppConfig


class RecrutamentoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "recrutamento"

    def ready(self):
        import recrutamento.signals
