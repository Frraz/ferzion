from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Lead
from .serializers import LeadSerializer


# 🔐 Remove CSRF apenas para essa API (forma correta)
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    # ✅ API pública (landing page)
    permission_classes = [AllowAny]

    # ✅ Sem CSRF apenas aqui
    authentication_classes = [CsrfExemptSessionAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 💡 Aqui você pode enriquecer o lead (IP, user-agent, etc)
        lead = serializer.save()

        return Response(
            {
                "message": "Lead enviado com sucesso.",
                "id": lead.id,
            },
            status=status.HTTP_201_CREATED,
        )
