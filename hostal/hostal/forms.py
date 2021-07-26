#Django
from django import forms
from django.contrib.auth.models import User

"""
# Register Usuarios nuevos
class RegisterForm(forms.Form):
	username = forms.CharField(
		required=True, 
		min_length=4, 
		max_length=50,
		# aplicamos estilo a nuestro input con widget
		widget=forms.TextInput(attrs={
			'class':'form-control',
			'id':'username',
			})
		)
	
	email = forms.EmailField(
		required=True,
		widget=forms.EmailInput(attrs={
			'class':'form-control',
			'id':'email',
			'placeholder':'micorreo@empresa.com'
			})
		)
		
	password = forms.CharField(
		required=True,
		widget=forms.PasswordInput(attrs={
			'class':'form-control',
			'id':'password',
			})
			)

	password2 = forms.CharField(
		label='Confirmar password',
		required=True,
		widget=forms.PasswordInput(attrs={
			'class':'form-control',
			})
		)


	def clean_username(self):
		#obtenemos los inputs del formulario
		username = self.cleaned_data.get('username')
		#consultamos si existen en db
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('El username ya se encuentra en uso')
		# de no existir
		return username


	def clean_email(self):
		#obtenemos los inputs del formulario
		email = self.cleaned_data.get('email')
		#consultamos si existen en db
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('El email ya se encuentra en uso')
		# de no existir
		return email

 
	# Validamos la igualdad de password y password2
	def clean(self):
		cleaned_data = super().clean()

		if cleaned_data.get('password2') != cleaned_data.get('password'):
			self.add_error('password2', 'El password no coincide')

    
    # método para crear nuevos usuarios
	def save(self):
		return User.objects.create_user(
    		self.cleaned_data.get('username'),
    		self.cleaned_data.get('email'),
    		self.cleaned_data.get('password')
    		)

   """