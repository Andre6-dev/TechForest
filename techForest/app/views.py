from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from api.models import *
from .forms import *

# Pagina principal
def index(request):
    context = {}
    return render(request, 'principal/index.html', context)

def planes(request):
    context = {}
    return render(request, 'principal/planes.html', context)

def soluciones(request):
    context = {}
    return render(request, 'principal/soluciones.html', context)

def nosotros(request):
    context = {}
    return render(request, 'principal/about_us.html', context)

def contacto(request):
    context = {}
    return render(request, 'principal/contacto.html', context)

# Dashboard Cliente
def cliente(request, cliente_id):
    cliente = get_object_or_404(Usuarios, pk=cliente_id)
    plan = Planes.objects.get(usuarios_id=cliente_id)
    return render(request, 'cliente/index.html', {'cliente': cliente,'plan': plan})

def perfilCliente(request, cliente_id):
    cliente = get_object_or_404(Usuarios, pk=cliente_id)
    form = UsuarioForm(request.POST or None, instance = cliente)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/cliente/"+str(cliente_id)+"/perfil")
    
    return render(request, 'cliente/perfil.html', {'cliente': cliente,'form':form})

def planCliente(request, cliente_id):
    cliente = get_object_or_404(Usuarios, pk=cliente_id)
    plan = Planes.objects.get(usuarios_id=cliente_id)
    pagos = Pagos.objects.filter(planes_id=plan.id)
    return render(request, 'cliente/plan.html', {'cliente': cliente,'plan': plan,'pagos': pagos})

def solucionCliente(request, cliente_id):
    cliente = get_object_or_404(Usuarios, pk=cliente_id)
    diapositivo = Dispositivos.objects.get(usuarios_id=cliente_id)
    opciones = Opciones.objects.get(diapositivos_id=diapositivo.id)
    return render(request, 'cliente/solucion.html', {'cliente': cliente,'opciones': opciones})

def dispositivoCliente(request, cliente_id):
    cliente = get_object_or_404(Usuarios, pk=cliente_id)
    dispositivo = Dispositivos.objects.get(usuarios_id=cliente_id)
    return render(request, 'cliente/dispositivo.html', {'cliente': cliente,'dispositivo': dispositivo})

def reportarCliente(request, cliente_id):
    cliente = get_object_or_404(Usuarios, pk=cliente_id)
    form = ErrorForm(request.POST or None)
    if form.is_valid():
        error = form.save(commit=False)
        error.usuarios = cliente
        form.save()
        return HttpResponseRedirect("/cliente/"+str(cliente_id)+"/reportar")
    
    return render(request, 'cliente/reportar.html', {'cliente': cliente,'form':form})

def reportesCliente(request, cliente_id):
    cliente = get_object_or_404(Usuarios, pk=cliente_id)
    errores = Errores.objects.filter(usuarios_id=cliente.id)
    return render(request, 'cliente/reportes.html', {'cliente': cliente,'errores': errores})

# Dashboard Administrador
def admin_dashboard(request):
    context = {}
    return render(request, 'administrador/admin_dashboard.html', context)


def administradores(request):
    context = {}
    return render(request, 'administrador/administradores.html', context)


def ayuda(request):
    context = {}
    return render(request, 'administrador/ayuda.html', context)


def dispositivos(request):
    context = {}
    return render(request, 'administrador/dispositivos.html', context)


def usuarios(request):
    context = {}
    return render(request, 'administrador/usuarios.html', context)