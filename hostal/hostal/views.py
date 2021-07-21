# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# User para dar de alta nuevos usuarios
from django.contrib.auth.models import User

# llamamos a la clase RegisterForm desde forms.py
from .forms import RegisterForm

# products
#from products.models import Product



def index(request):
	return render(request,'index.html', {})



def login_usuario(request):
	# si el usuario esta logeado, evitamos que vaya a login desde el navegador
	if request.user.is_authenticated:
		return redirect('index')
    
    # si el método usado es POST obtenemos sus valores 
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		# autenticamos al usuario con los valores dados en POST
		user = authenticate(username=username, password=password)
		if user:
			# Usamos funcion login de Django para verificar datos en DB
			login(request,user)
			# una vez logeado enviamos un mensaje
			messages.success(request, 'Bienvenido {}'.format(user.username))
			return redirect('index')
		else:
			messages.error(request, 'Usuario o contraseña no validos')

	return render(request, 'login.html', {})



def logout_usuario(request):
	logout(request)
	messages.success(request, 'Sesión cerrada exitosamente')
	return redirect('login_usuario')


def registro_usuario(request):
	# si el usuario esta logeado, evitamos que vaya a registro desde el navegador
	if request.user.is_authenticated:
		return redirect('index')

	#Generamos una instacia de RegisterForm para usar como formulario 
	form = RegisterForm(request.POST or None)
    
    # validamos los datos del formulario
	if request.method == 'POST' and form.is_valid():
        # obtenemos los datos del formulario y lo validamos en RegisterForm
		user = form.save()
		if user:
			#logeamos y redirigimos
			login(request, user)
			messages.success(request, 'Usuario creado exitosamente')
			return redirect('index')

	return render(request, 'registro.html', {'form':form}) 