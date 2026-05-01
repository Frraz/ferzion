from rest_framework import generics, status
from rest_framework.response import Response

from .models import Lead
from .serializers import LeadSerializer


class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Lead enviado com sucesso."},
            status=status.HTTP_201_CREATED,
        )
