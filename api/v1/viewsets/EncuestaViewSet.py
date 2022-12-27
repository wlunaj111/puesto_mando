from api.models.Encuesta import Encuesta
from api.v1.serializer.encuesta.EncuestaSerializer import EncuestaSerializer
from rest_framework import viewsets, status, permissions

class EncuestaViewSet(viewsets.ModelViewSet):
    queryset = Encuesta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EncuestaSerializer