from decouple import config
from djoser import email


class PasswordResetEmail(email.PasswordResetEmail):
    template_name = "registration/email/password_reset.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["domain"] = config("DOMAIN_FRONT", default=context["domain"])
        context["site_name"] = ".ndt"
        return context
