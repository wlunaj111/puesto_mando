from rest_framework import serializers
from api.models.Encuesta import Encuesta


class EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields = '__all__'