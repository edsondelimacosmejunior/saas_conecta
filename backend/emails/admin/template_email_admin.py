from django.contrib import messages
from django.contrib import admin
from emails.admin.anexo_email_inline import AnexoEmailInline
from emails.models.mensagem_email import MensagemEmail
from unfold.admin import ModelAdmin
from ..models import TemplateEmail
from import_export.forms import SelectableFieldsExportForm
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from unfold.decorators import action
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

@admin.register(TemplateEmail)
class TemplateEmailAdmin(ModelAdmin):
    list_display = [
        'id',
        'assunto',
        'codigo'
    ]

    search_fields = [
        'id',
        'assunto',
        'codigo'
    ]

    filter_horizontal = [
        'destinatarios',
        'enviar_copia_oculta',
    ]

    exclude = [
        'legenda_email',
        'titulo_alteracao_email'
    ]

    inlines = [
        AnexoEmailInline,
    ]
    export_form_class = SelectableFieldsExportForm

    formfield_overrides = {
        HTMLField: {"widget": TinyMCE},
    }
    

    actions_detail = ["enviar_email"]

    @action(description="Enviar E-mail")
    def enviar_email(self, request, object_id):
        # Pega o objeto
        obj = self.get_object(request, object_id)

        # Chama a função de envio de e-mail
        mensagem = MensagemEmail.objects.create(template_email=obj)
        mensagem.gerar_historico()
        
        # Chama enviar passando os destinatários extra
        mensagem.enviar()

        # Mostra mensagem de sucesso no topo da página
        self.message_user(request, "E-mail enviado com sucesso!", level=messages.SUCCESS)

        
        # Redireciona para a mesma página do objeto
        return redirect(reverse_lazy('admin:emails_templateemail_change', args=[object_id]))



   # Organizando os campos em grupos (fieldsets)
    fieldsets = (
        ("Informações básicas", {
            "fields": (
                "nome_interno",
                "codigo",
                "ativo",
                "assunto",
                "texto_acima_titulo",
                "titulo_email",
                # "titulo_alteracao_email",
                # "legenda_email",
            )
        }),
        ("Corpo do e-mail", {
            "fields": ("corpo_email",),
        }),
        ("Destinatários e envio", {
            "fields": (
                "destinatarios",
                "enviar_copia_oculta",
                "enviar_usuario_criacao",
                "responder_para",
            )
        }),
        ("Links adicionais", {
            "fields": (
                "primeiro_link",
                "texto_primeiro_link",
                "segundo_link",
                "texto_segundo_link",
            )
        }),
        ("Configurações avançadas", {
            "fields": ("smtp_especifico", "tipo_objeto", "logo_superior"),
        }),
    )