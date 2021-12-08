from django.urls import path
from .views import lista_corsi
urlpatterns = [
    path("", lista_corsi)
]