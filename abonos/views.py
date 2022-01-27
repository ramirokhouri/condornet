# Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# App
from .models import Cliente, Cobrador, Abono, Recaudacion
from .forms import ClienteForm, CobradorForm, AbonoForm, RecaudacionForm


# Create your views here.

# Generales
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            usuario = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe')
        
        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o Contraseña incorrectos')

    context = {}
    return render(request, 'paginas/loginsesion.html',context)
def logoutUsuario(request):
    logout(request)
    return redirect('inicio')
def inicio(request):
    return render(request, 'paginas/inicio.html')

# Clientes
def clientes(request):
    clientes = Cliente.objects.all()
    clientes_cuenta = clientes.count()
    context = {
        'clientes': clientes,
        'clientes_cuenta': clientes_cuenta
    }
    return render(request, 'clientes/index.html', context)
@login_required(login_url='login')
def agregar_cliente(request):
    formulario = ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/crear.html', {'formulario': formulario})
@login_required(login_url='login')
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    formulario = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
    context = {
        'formulario': formulario,
        'cliente': cliente
    }
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/editar.html', context)
@login_required(login_url='login')
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')

# Cobradores
def cobradores(request):
    cobradores = Cobrador.objects.all()
    cobradores_cuenta = cobradores.count()
    context = {
        'cobradores': cobradores,
        'cobradores_cuenta': cobradores_cuenta
    }
    return render(request, 'cobradores/index.html', context)
@login_required(login_url='login')
def agregar_cobrador(request):
    formulario = CobradorForm(request.POST or None, request.FILES or None)
    usuarios = User.objects.all()
    context = {
        'formulario': formulario,
        'usuarios': usuarios
    }
    if formulario.is_valid():
        formulario.save()
        return redirect('cobradores')
    return render(request, 'cobradores/crear.html', context)
@login_required(login_url='login')
def editar_cobrador(request, id):
    cobrador = Cobrador.objects.get(id=id)
    usuarios = User.objects.all()
    formulario = CobradorForm(request.POST or None, request.FILES or None, instance=cobrador)
    context = {
        'formulario': formulario,
        'usuarios': usuarios,
        'cobrador': cobrador
    }
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('cobradores')
    return render(request, 'cobradores/editar.html', context)
@login_required(login_url='login')
def eliminar_cobrador(request, id):
    cobrador = Cobrador.objects.get(id=id)
    cobrador.delete()
    return redirect('cobradores')

# Recaudacion
def recaudaciones(request):

    # filtro cobrador
    if request.GET.get('query_cobrador') != None:
        query_cobrador = request.GET.get('query_cobrador')
        recaudaciones = Recaudacion.objects.filter(cobrador__id=query_cobrador)

    # filtro mes
    if request.GET.get('query_mes') != None:
        query_mes = request.GET.get('query_mes')
        recaudaciones = Recaudacion.objects.filter(fecha__month=query_mes)

    if request.GET.get('query_cobrador') == None and request.GET.get('query_mes') == None:
        recaudaciones = Recaudacion.objects.all()
    
    cobradores = Cobrador.objects.all()
    return render(request, 'recaudaciones/index.html', {'recaudaciones': recaudaciones,
    'cobradores': cobradores
    })
@login_required(login_url='login')
def agregar_recaudacion(request):
    cobradores = Cobrador.objects.all()
    formulario = RecaudacionForm(request.POST or None, request.FILES or None)
    context = {
        'formulario': formulario,
        'cobradores': cobradores
    }
    if formulario.is_valid():
        formulario.save()
        return redirect('recaudaciones')
    return render(request, 'recaudaciones/crear.html', context)
@login_required(login_url='login')
def editar_recaudacion(request, id):
    recaudacion = Recaudacion.objects.get(id=id)
    formulario = RecaudacionForm(request.POST or None, request.FILES or None, instance=recaudacion)
    context = {
        'formulario':formulario,
        'recaudacion': recaudacion
    }
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('recaudaciones')
    return render(request, 'recaudaciones/editar.html', context)
@login_required(login_url='login')
def eliminar_recaudacion(request, id):
    recaudacion = Recaudacion.objects.get(id=id)
    recaudacion.delete()
    return redirect('recaudaciones')

# Abonos
def abonos(request):

    # filtro cobrador
    if request.GET.get('query_cobrador') != None:
        query_cobrador = request.GET.get('query_cobrador')
        abonos = Abono.objects.filter(cobrador__id = query_cobrador)
    
    # filtro mes
    if request.GET.get('query_mes') != None:
        query_mes = request.GET.get('query_mes')
        abonos = Abono.objects.filter(fecha__month = query_mes)

    #filtro cliente
    if request.GET.get('query_cliente') != None:
        query_cliente = request.GET.get('query_cliente')
        abonos = Abono.objects.filter(cliente__id = query_cliente)
    
    if request.GET.get('query_cliente') == None and request.GET.get('query_cobrador') == None and request.GET.get('query_mes') == None:
        abonos = Abono.objects.all()
    
    cobradores = Cobrador.objects.all()
    return render(request, 'abonos/index.html', {'abonos': abonos,
    'cobradores': cobradores
    })
@login_required(login_url='login')
def agregar_abono(request):
    cobradores = Cobrador.objects.all()
    clientes = Cliente.objects.all()
    formulario = AbonoForm(request.POST or None, request.FILES or None)
    context = {
        'formulario': formulario,
        'cobradores': cobradores,
        'clientes': clientes,
    }
    if formulario.is_valid():
        formulario.save()
        return redirect('abonos')
    return render(request, 'abonos/crear.html', context)
@login_required(login_url='login')
def editar_abono(request, id):
    abono = Abono.objects.get(id=id)
    formulario = AbonoForm(request.POST or None, request.FILES or None, instance=abono)
    cobradores = Cobrador.objects.all()
    clientes = Cliente.objects.all()
    context = {
        'formulario':formulario,
        'cobradores':cobradores,
        'clientes':clientes,
        'abono':abono
    }
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('abonos')
    return render(request, 'abonos/editar.html', context)
@login_required(login_url='login')
def eliminar_abono(request, id):
    abono = Abono.objects.get(id=id)
    abono.delete()
    return redirect('abonos')