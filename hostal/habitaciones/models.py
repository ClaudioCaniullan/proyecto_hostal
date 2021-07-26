# models app habitaciones
from django.db import models
from django.core import validators


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




class Usuario(models.Model):

	rutUsuario = models.CharField(max_length =10, primary_key=True, default=None,
		validators=[validators.MinLengthValidator(9, "Ingresar dni en el siguiente formato 77111666-5"), 
		validators.MaxLengthValidator(10, "Ingresar dni en el siguiente formato 77111666-5")]
                    )

	username = models.CharField(max_length=20)
	email = models.EmailField(max_length=20)
	password = models.CharField(max_length=10)
	#password2 = models.CharField(max_length=10)
	nom_hab = models.ForeignKey(Habitaciones, on_delete=models.CASCADE)
	