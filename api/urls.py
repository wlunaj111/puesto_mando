from django.urls import path, include
import api.v1.urls


urlpatterns = [
    path('v1/', include(api.v1.urls)),
]
