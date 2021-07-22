# views app habitaciones

#Django
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Habitaciones


# Vista del usuario
class HabitacionesListView(ListView):
	template_name = 'index.html'
	queryset = Habitaciones.objects.all().order_by('-id')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


# CRUD Habitaciones FALTA IMPLEMENTAR EN EL TEMPLATES ADMINISTRADOR
# fields = [nombre, descripcion, precio, estado, imagen]

class AdministradorListView(ListView):
	model = Habitaciones
	fields='__all__'
	template_name = 'admin.html'

class AdministradorUpdateView(UpdateView):
	model = Habitaciones
	fields='__all__'
	template_name = 'admin.html'

class AdministradorDeleteView(DeleteView):
	model = Habitaciones
	fields='__all__'
	template_name = 'admin.html'