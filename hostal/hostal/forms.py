from django import forms
from django.contrib.auth.models import User

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
		# aplicamos estilo a nuestro input con widget
		widget=forms.EmailInput(attrs={
			'class':'form-control',
			'id':'email',
			'placeholder':'micorreo@empresa.com'
			})
		)
		
	password = forms.CharField(
		required=True,
		# aplicamos estilo a nuestro input con widget
		widget=forms.PasswordInput(attrs={
			'class':'form-control',
			'id':'password',
			})
			)

	password2 = forms.CharField(
		label='Confirmar password',
		required=True,
		# aplicamos estilo a nuestro input con widget
		widget=forms.PasswordInput(attrs={
			'class':'form-control',
			})
		)