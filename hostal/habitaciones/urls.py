# urls app habitaciones
from django.urls import path

from . import views

app_name = 'habitaciones'
# Usaremos modelos como vistas
urlpatterns = [
   path('listar_hab', views.HabitacionesListView.as_view(), name='listar_hab'),
   path('editar_hab/<pk>', views.HabitacionesUpdateView.as_view(), name='editar_hab'),
   path('eliminar_hab/<pk>', views.HabitacionesDeleteView.as_view(), name='eliminar_hab'),
   path('crear_hab', views.HabitacionesCreateView.as_view(), name='crear_hab'),
]