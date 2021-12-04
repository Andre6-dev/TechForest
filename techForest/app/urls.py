from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('planes', views.planes, name='planes'),
    path('soluciones', views.soluciones, name='soluciones'),
    path('cliente', views.cliente, name='cliente'),
    path('cliente/perfil', views.perfilCliente, name='perfilCliente'),
    path('cliente/plan', views.planCliente, name='planCliente'),
    path('cliente/solucion', views.solucionCliente, name='solucionCliente'),
    path('cliente/contacto', views.contactoCliente, name='contactoCliente')
]