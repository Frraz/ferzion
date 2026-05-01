from django.db import models


class Lead(models.Model):
    class Segmento(models.TextChoices):
        AGRO = "agro", "Agronegócio"
        LOGISTICA = "logistica", "Logística"
        INDUSTRIA = "industria", "Indústria"
        VAREJO = "varejo", "Varejo"
        OUTRO = "outro", "Outro"

    nome = models.CharField("Nome", max_length=255)
    email = models.EmailField("E-mail", blank=True, null=True)  # ✅ NOVO
    whatsapp = models.CharField("WhatsApp", max_length=30)

    segmento = models.CharField(
        "Segmento",
        max_length=50,
        choices=Segmento.choices,
        default=Segmento.OUTRO,
        blank=True,
    )

    desafio = models.TextField("Desafio", blank=True)

    # Extras
    ip = models.GenericIPAddressField("IP", null=True, blank=True)
    user_agent = models.TextField("User Agent", null=True, blank=True)

    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    def __str__(self):
        return f"{self.nome} ({self.whatsapp})"
