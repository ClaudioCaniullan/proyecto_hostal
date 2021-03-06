"""hostal URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

# importamos las view que se encuentran en este modulo
from . import views

# impostamos las views de la app habitaciones
from habitaciones.views import HabitacionesListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HabitacionesListView.as_view(), name='index'),
    path('administrador', HabitacionesListView.as_view(), name='administrador'),
    path('login_usuario', views.login_usuario, name='login_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
    path('registro_usuario', views.registro_usuario, name='registro_usuario'),
    path('administrador', include('habitaciones.urls')),
]

# indicamos a Django donde trabajar con nuestra imagenes
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)