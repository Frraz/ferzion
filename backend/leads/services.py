from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.timezone import now


def send_lead_confirmation_email(lead):
    if not lead.email:
        return  # não envia se não tiver email

    subject = "Recebemos seu contato 🚀"

    context = {
        "nome": lead.nome,
        "whatsapp": lead.whatsapp,
        "segmento": lead.get_segmento_display() if lead.segmento else "",
        "desafio": lead.desafio,
        "year": now().year,
    }

    html_content = render_to_string(
        "emails/lead_confirmation.html",
        context,
    )

    email = EmailMultiAlternatives(
        subject=subject,
        body="Recebemos seu contato. Em breve retornaremos.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[lead.email],
    )

    email.attach_alternative(html_content, "text/html")

    # evita quebrar request se email falhar
    try:
        email.send()
    except Exception as e:
        print("Erro ao enviar email:", e)
