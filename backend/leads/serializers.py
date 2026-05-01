from rest_framework import serializers

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=False,
        allow_null=True,
        allow_blank=True,
    )

    class Meta:
        model = Lead
        fields = [
            "nome",
            "email",
            "whatsapp",
            "segmento",
            "desafio",
        ]

    # 🔹 Nome obrigatório e limpo
    def validate_nome(self, value):
        value = value.strip()

        if len(value) < 2:
            raise serializers.ValidationError("Nome muito curto.")

        return value

    # 🔹 Email opcional, mas válido se enviado
    def validate_email(self, value):
        if not value:
            return None

        return value.strip().lower()

    # 🔹 WhatsApp validado
    def validate_whatsapp(self, value):
        value = value.strip()

        numbers = "".join(filter(str.isdigit, value))

        if len(numbers) < 10:
            raise serializers.ValidationError("WhatsApp inválido.")

        return numbers

    # 🔹 Segmento tolerante (não quebra)
    def validate_segmento(self, value):
        if not value:
            return Lead.Segmento.OUTRO

        valid_values = [choice[0] for choice in Lead.Segmento.choices]

        if value not in valid_values:
            return Lead.Segmento.OUTRO

        return value

    # 🔹 Desafio opcional
    def validate_desafio(self, value):
        if not value:
            return ""

        return value.strip()

    # 🔥 EXTRA: normalização geral (opcional mas top)
    def validate(self, attrs):
        # garante que pelo menos um contato exista
        if not attrs.get("email") and not attrs.get("whatsapp"):
            raise serializers.ValidationError(
                "Informe pelo menos um meio de contato (email ou WhatsApp)."
            )

        return attrs
