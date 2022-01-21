# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse

# App
from .models import Cliente, Cobrador, Abono, Recaudacion
from .forms import ClienteForm, CobradorForm, AbonoForm, RecaudacionForm


# Create your views here.

# Generales
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

# Clientes
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/index.html', {'clientes': clientes})
def agregar_cliente(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/crear.html', {'formulario': formulario})
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    formulario = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/editar.html', {'formulario': formulario})
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')

# Cobradores
def cobradores(request):
    cobradores = Cobrador.objects.all()
    return render(request, 'cobradores/index.html', {'cobradores': cobradores})
def agregar_cobrador(request):
    formulario = CobradorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('cobradores')
    return render(request, 'cobradores/crear.html', {'formulario': formulario})
def editar_cobrador(request, id):
    cobrador = Cobrador.objects.get(id=id)
    formulario = CobradorForm(request.POST or None, request.FILES or None, instance=cobrador)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('cobradores')
    return render(request, 'cobradores/editar.html', {'formulario': formulario})
def eliminar_cobrador(request, id):
    cobrador = Cobrador.objects.get(id=id)
    cobrador.delete()
    return redirect('cobradores')

# Recaudacion
def recaudaciones(request):
    recaudaciones = Recaudacion.objects.all()
    return render(request, 'recaudaciones/index.html', {'recaudaciones': recaudaciones})
def agregar_recaudacion(request):
    formulario = RecaudacionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('recaudaciones')
    return render(request, 'recaudaciones/crear.html', {'formulario': formulario})
def editar_recaudacion(request, id):
    recaudacion = Recaudacion.objects.get(id=id)
    formulario = RecaudacionForm(request.POST or None, request.FILES or None, instance=recaudacion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('recaudaciones')
    return render(request, 'recaudaciones/editar.html', {'formulario': formulario})
def eliminar_recaudacion(request, id):
    recaudacion = Recaudacion.objects.get(id=id)
    recaudacion.delete()
    return redirect('recaudaciones')

# Abonos
def abonos(request):
    abonos = Abono.objects.all()
    return render(request, 'abonos/index.html', {'abonos': abonos})
def agregar_abono(request):
    formulario = AbonoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('abonos')
    return render(request, 'abonos/crear.html', {'formulario': formulario})
def editar_abono(request, id):
    abono = Abono.objects.get(id=id)
    formulario = AbonoForm(request.POST or None, request.FILES or None, instance=abono)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('abonos')
    return render(request, 'abonos/editar.html', {'formulario': formulario})
def eliminar_abono(request, id):
    abono = Abono.objects.get(id=id)
    abono.delete()
    return redirect('abonos')