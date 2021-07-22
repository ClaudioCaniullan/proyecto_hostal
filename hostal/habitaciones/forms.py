# forms app habitaciones
from django import forms
from .models import Habitaciones
#from django.forms import widgets


# Definimos un Form a partir del model Habitaciones para usar en CRUD
class HabitacionesForms(forms.ModelForm):
    
    class Meta:
        model = Habitaciones
        fields = '__all__'