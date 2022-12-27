from django.db import models

class Encuesta(models.Model):
    nombre = models.TextField()
    apellidos = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)