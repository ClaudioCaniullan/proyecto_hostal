# urls app habitaciones
from django.urls import path

from .views import HabitacionesListView, HabitacionesUpdateView, HabitacionesDeleteView, HabitacionesCreateView

app_name = 'habitaciones'
# Usaremos modelos como vistas
urlpatterns = [
   path('listar_hab', HabitacionesListView.as_view(), name='listar_hab'),
   path('editar_hab', HabitacionesUpdateView.as_view(), name='editar_hab'),
   path('eliminar_hab', HabitacionesDeleteView.as_view(), name='eliminar_hab'),
   path('crear_hab', HabitacionesCreateView.as_view(), name='crear_hab'),
]