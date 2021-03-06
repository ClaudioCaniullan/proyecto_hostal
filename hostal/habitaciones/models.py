# models app habitaciones
from django.db import models


# Create your models here.
class Habitaciones(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
	estados = [
	        ('D', 'Disponible'), 
	        ('O', 'Ocupado'),
	        ('M', 'En Mantencion')]
	estado = models.CharField(max_length=1,choices=estados, default='D')
	image = models.ImageField(upload_to='habitaciones', null=False, blank=False)

	def __str__(self):
		return self.nombre