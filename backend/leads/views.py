from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Lead
from .serializers import LeadSerializer
from .services import send_lead_confirmation_email


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

        # 🔥 Captura dados extras
        ip = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT", "")

        lead = serializer.save(
            ip=ip,
            user_agent=user_agent,
        )

        # =========================
        # 📧 ENVIO DE EMAIL (CORRETO)
        # =========================
        try:
            send_lead_confirmation_email(lead)
        except Exception as e:
            # Loga erro mas não quebra API
            print("Erro ao enviar email:", e)

        return Response(
            {
                "message": "Lead enviado com sucesso.",
                "id": lead.id,
            },
            status=status.HTTP_201_CREATED,
        )
