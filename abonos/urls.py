""" Abonos urls. """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUsuario, name='logout'),

    # clientes
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar_cliente/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:id>', views.eliminar_cliente, name='eliminar_cliente'),
    path('editar_cliente/<int:id>', views.editar_cliente, name='editar_cliente'),

    # abonos
    path('abonos/', views.abonos, name='abonos'),
    path('abonos/agregar_abono/', views.agregar_abono, name='agregar_abono'),
    path('abonos/editar_abono/', views.editar_abono, name='editar_abono'),
    path('eliminar_abono/<int:id>', views.eliminar_abono, name='eliminar_abono'),
    path('editar_abono/<int:id>', views.editar_abono, name='editar_abono'),

    # recaudacion
    path('recaudaciones/', views.recaudaciones, name='recaudaciones'),
    path('recaudaciones/agregar_recaudacion/', views.agregar_recaudacion, name='agregar_recaudacion'),
    path('recaudaciones/editar_recaudacion/', views.editar_recaudacion, name='editar_recaudacion'),
    path('eliminar_recaudacion/<int:id>', views.eliminar_recaudacion, name='eliminar_recaudacion'),
    path('editar_recaudacion/<int:id>', views.editar_recaudacion, name='editar_recaudacion'),

    # cobradores
    path('cobradores/', views.cobradores, name='cobradores'),
    path('cobradores/agregar_cobrador/', views.agregar_cobrador, name='agregar_cobrador'),
    path('cobradores/editar_cobrador/', views.editar_cobrador, name='editar_cobrador'),
    path('eliminar_cobrador/<int:id>', views.eliminar_cobrador, name='eliminar_cobrador'),
    path('editar_cobrador/<int:id>', views.editar_cobrador, name='editar_cobrador'),
]