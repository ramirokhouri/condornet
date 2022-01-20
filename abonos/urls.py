""" Abonos urls. """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),

    # clientes
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar_cliente/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:id>', views.eliminar_cliente, name='eliminar_cliente'),
    path('editar_cliente/<int:id>', views.editar_cliente, name='editar_cliente'),

    # abonos

    # recaudacion

    # cobradores
]