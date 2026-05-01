import logging

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.timezone import now

logger = logging.getLogger(__name__)


def send_lead_confirmation_email(lead):
    """
    Envia email de confirmação para o lead.
    Seguro, com fallback adequado e sem expor dados sensíveis.
    """

    if not lead.email:
        return  # não envia se não tiver email

    subject = "Recebemos seu contato 🚀"

    # 🔒 Contexto mínimo (evita vazamento de dados do formulário)
    context = {
        "nome": lead.nome,
        "year": now().year,
    }

    try:
        # HTML principal
        html_content = render_to_string(
            "emails/lead_confirmation.html",
            context,
        )

        # Texto fallback (clientes que não renderizam HTML)
        text_content = (
            f"Olá {lead.nome},\n\n"
            "Recebemos sua solicitação de diagnóstico.\n"
            "Em breve entraremos em contato com você.\n\n"
            "Equipe Ferzion"
        )

        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,  # 🔥 fallback correto
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[lead.email],
        )

        # versão HTML
        email.attach_alternative(html_content, "text/html")

        email.send()

    except Exception as e:
        logger.error(f"[EMAIL] Erro ao enviar confirmação do lead {lead.id}: {e}")
