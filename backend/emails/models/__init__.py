from emails.models.anexo_email import AnexoEmail
from .configuracao_email import ConfiguracaoEmail
from .destinatario import Destinatario
from .mensagem_email import MensagemEmail
from .template_email import TemplateEmail

all = [
    TemplateEmail, 
    Destinatario, 
    MensagemEmail, 
    ConfiguracaoEmail,
    AnexoEmail
]

