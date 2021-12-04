from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'principal/index.html', context)

def planes(request):
    context = {}
    return render(request, 'principal/planes.html', context)

def soluciones(request):
    context = {}
    return render(request, 'principal/soluciones.html', context)

def cliente(request):
    context = {}
    return render(request, 'cliente/index.html', context)

def perfilCliente(request):
    context = {}
    return render(request, 'cliente/perfil.html', context)

def planCliente(request):
    context = {}
    return render(request, 'cliente/plan.html', context)

def solucionCliente(request):
    context = {}
    return render(request, 'cliente/solucion.html', context)

def contactoCliente(request):
    context = {}
    return render(request, 'cliente/contacto.html', context)
