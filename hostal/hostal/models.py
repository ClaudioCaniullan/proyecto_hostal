# models hostal
from django.db import models

from habitaciones.models import habitaciones

class Usuario(models.Model):
	username = models.CharField()
	email = models.EmailField()
	password = models.CharField()
	password2 = models.CharField()
	habitacion = models.ForeignKey(habitacion, on_delete=models.CASCADE)