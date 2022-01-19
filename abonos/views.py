# Django
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente


# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/index.html', {'clientes': clientes})

def agregar_cliente(request):
    return render(request, 'clientes/crear.html')

def editar_cliente(request):
    return render(request, 'clientes/editar.html')