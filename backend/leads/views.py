from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Lead
from .serializers import LeadSerializer


# 🔐 Remove CSRF apenas para essa API
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    permission_classes = [AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 🔥 captura dados extras
        ip = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT", "")

        lead = serializer.save(
            ip=ip,
            user_agent=user_agent,
        )

        # =========================
        # 📧 ENVIO DE EMAIL
        # =========================
        email = getattr(lead, "email", None)

        if email:
            try:
                send_mail(
                    subject="Recebemos seu contato 🚀",
                    message=(
                        f"Olá {lead.nome},\n\n"
                        "Recebemos sua solicitação com sucesso!\n"
                        "Nossa equipe vai analisar e entrar em contato em breve.\n\n"
                        "Se precisar de algo urgente, responda este e-mail.\n\n"
                        "— Equipe Ferzion"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=True,  # não quebra sua API
                )
            except Exception:
                pass  # evita quebrar a API em caso de erro de email

        return Response(
            {
                "message": "Lead enviado com sucesso.",
                "id": lead.id,
            },
            status=status.HTTP_201_CREATED,
        )
