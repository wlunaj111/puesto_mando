from django.urls import path, include
from rest_framework import routers


from api.v1.viewsets.EncuestaViewSet import EncuestaViewSet

router = routers.DefaultRouter()
# rutas de v1
router.register(r'encuesta', EncuestaViewSet, basename='Encuesta')


urlpatterns = [
    path('', include(router.urls), ),
]