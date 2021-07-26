# views app habitaciones

#Django
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Habitaciones, Usuario


"""# Vista del usuario
class HabitacionesListView(ListView):
	template_name = 'index2.html'
	queryset = Habitaciones.objects.all().order_by('-id')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
"""

# CRUD Habitaciones FALTA IMPLEMENTAR EN EL TEMPLATES ADMINISTRADOR
# fields = [nombre, descripcion, precio, estado, imagen]

class HabitacionesListView(ListView):
	model = Habitaciones
	fields='__all__'
	#template_name = 'habitaciones_list.html'
	success_url=reverse_lazy('habitaciones:listar_hab')

class HabitacionesUpdateView(UpdateView):
	model = Habitaciones
	fields='__all__'
	#template_name = 'admin2.html'
	success_url=reverse_lazy('habitaciones:listar_hab')

class HabitacionesDeleteView(DeleteView):
	model = Habitaciones
	fields='__all__'
	#template_name = 'admin.html'
	success_url=reverse_lazy('habitaciones:listar_hab')