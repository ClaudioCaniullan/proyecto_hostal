# views app habitaciones

#Django
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Habitaciones, Usuario
from .forms import HabitacionesForms


"""# Vista del usuario
class HabitacionesListView(ListView):
	template_name = 'index2.html'
	queryset = Habitaciones.objects.all().order_by('-id')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context
"""

# CRUD Habitaciones 
# fields = [nombre, descripcion, precio, estado, imagen]

class HabitacionesListView(ListView):
	model = Habitaciones
	#fields='__all__'
	template_name = 'habitaciones/habitaciones_list.html'

class HabitacionesCreateView(CreateView):
	model = Habitaciones
	form_class = HabitacionesForms
	template_name = 'habitaciones/habitaciones_form.html'
	success_url=reverse_lazy('habitaciones:listar_hab')

class HabitacionesUpdateView(UpdateView):
	model = Habitaciones
	form_class = HabitacionesForms
	template_name = 'habitaciones/habitaciones_form.html'
	success_url=reverse_lazy('habitaciones:listar_hab')

class HabitacionesDeleteView(DeleteView):
	model = Habitaciones
	template_name = 'habitaciones/habitaciones_delete.html'
	success_url=reverse_lazy('habitaciones:listar_hab')