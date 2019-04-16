from rest_framework import serializers

from .models import GCAAffaire


class GCAAffaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = GCAAffaire
        fields = "__all__"