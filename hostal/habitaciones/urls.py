# urls app habitaciones
from django.urls import path

from . import views

# Usaremos modelos como vistas
urlpatterns = [
   path('administrador', views.AdministradorListView.as_view(), name='administrador')
]