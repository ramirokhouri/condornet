"""Abonos models."""

# Django
from django.db import models
from django.db.models.deletion import DO_NOTHING, SET_NULL
from django.contrib.auth.models import User

from datetime import datetime

class Cliente(models.Model):
    """Modelo Clientes"""

    apellido = models.CharField(max_length=45, verbose_name="apellido")
    nombre = models.CharField(max_length=45, verbose_name="nombre")

    activo = models.BooleanField(default=True, verbose_name="activo")

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = self.apellido + ", " + self.nombre
        return fila
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-modificado', '-creado']

class Cobrador(models.Model):
    """Modelo Cobradores"""

    nombre = models.CharField(max_length=45, verbose_name="nombre")

    activo = models.BooleanField(default=True, verbose_name="activo")

    usuario = models.ForeignKey(User,null=True, on_delete=SET_NULL)

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cobrador"
        verbose_name_plural = "Cobradores"
        ordering = ['-modificado', '-creado']

class Abono(models.Model):
    """Modelo Abonos"""
    cliente = models.ForeignKey(
        'Cliente',
        null=True,
        on_delete=SET_NULL
        )
    cobrador = models.ForeignKey(
        'Cobrador',
        null=True,
        on_delete=SET_NULL
        )
    
    fecha = models.DateTimeField(
        blank=True,
        null=True,
        default= datetime.now,
        verbose_name="fecha"
        )
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="monto"
        )
    nota = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="nota"
        )
    concepto = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="concepto"
        )

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = str(self.fecha) + ", " + str(self.monto) + ", " + self.cobrador.nombre
        return fila

    class Meta:
        verbose_name = "Abono"
        verbose_name_plural = "Abonos"
        ordering = ['-modificado', '-creado']

class Recaudacion(models.Model):
    """Modelo Recaudación"""

    cobrador = models.ForeignKey(
        'Cobrador',
        blank=False,
        null=True,
        on_delete=SET_NULL
        )
    
    fecha = models.DateTimeField(
        blank=True,
        null=True,
        default= datetime.now,
        verbose_name="fecha"
        )
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="monto"
        )
    nota = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="nota"
        )

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        fila = self.cobrador.nombre + ", " + str(self.fecha) + ", " + str(self.monto)
        return fila

    class Meta:
        verbose_name = "Recaudación"
        verbose_name_plural = "Recaudaciones"
        ordering = ['-modificado', '-creado']