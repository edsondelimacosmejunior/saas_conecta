
from emails.admin.anexo_email_admin import AnexoEmailAdmin
from emails.admin.configuracao_email_admin import ConfiguracaoEmailAdmin
from emails.admin.destinatario_admin import DestinatarioAdmin
from emails.admin.mensagem_email_admin import MensagemEmailAdmin
from emails.admin.template_email_admin import TemplateEmailAdmin


all = [
    DestinatarioAdmin,
    MensagemEmailAdmin,
    TemplateEmailAdmin,
    ConfiguracaoEmailAdmin,
    AnexoEmailAdmin
]

