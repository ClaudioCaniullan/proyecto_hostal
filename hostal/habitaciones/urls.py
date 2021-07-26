# urls app habitaciones
from django.urls import path

from . import views

# Usaremos modelos como vistas
urlpatterns = [
   path('listar_hab', views.HabitacionesListView.as_view(), name='listar_hab'),
   path('<pk>/delete_hab', views.HabitacionesDeleteView.as_view(), name='delete_hab'),
]