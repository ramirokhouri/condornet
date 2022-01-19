# Django
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def clientes(request):
    return render(request, 'clientes/index.html')

def agregar_cliente(request):
    return render(request, 'clientes/crear.html')

def editar_cliente(request):
    return render(request, 'clientes/editar.html')