# admin app habitaciones
from django.contrib import admin

# Register your models here.
from .models import Habitaciones, Usuario

admin.site.register(Habitaciones)
admin.site.register(Usuario)

