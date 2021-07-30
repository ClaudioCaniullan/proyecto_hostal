# views app habitaciones

#Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.template.response import TemplateResponse

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Habitaciones, Usuario
from .forms import HabitacionesForms


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
	context_object_name = 'habitaciones'

class HabitacionesDeleteView(DeleteView):
	model = Habitaciones
	template_name = 'habitaciones/habitaciones_delete.html'
	context_object_name = 'habitaciones'
	success_url=reverse_lazy('habitaciones:listar_hab')