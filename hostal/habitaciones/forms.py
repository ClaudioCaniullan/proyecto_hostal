# forms app habitaciones
from django import forms
from .models import *
from django.contrib.auth.models import User
#from django.forms import widgets


# Definimos un Form a partir del model Habitaciones para usar en CRUD
class HabitacionesForms(forms.ModelForm):
    
    class Meta:
        model = Habitaciones
        # fields = [nombre, descripcion, precio, estado, image]
        fields = '__all__'



class UsuarioForms(forms.ModelForm):
    
    class Meta:
        model = Usuario
        # fields = [username, email, password, password2, habiacion]
        fields = '__all__'