from django.db import models


class Lead(models.Model):
    SEGMENTOS = [
        ("agro", "Agronegócio"),
        ("logistica", "Logística"),
        ("industria", "Indústria"),
        ("varejo", "Varejo"),
        ("outro", "Outro"),
    ]

    nome = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=30)
    segmento = models.CharField(max_length=50, choices=SEGMENTOS)
    desafio = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.nome
