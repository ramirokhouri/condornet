"""Abonos models."""

# Django
from django.db import models
from django.db.models.deletion import DO_NOTHING, SET_NULL

class Cliente(models.Model):
    """Modelo Clientes"""

    apellido = models.CharField(max_length=45, verbose_name="apellido")
    nombre = models.CharField(max_length=45, verbose_name="nombre")

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True, verbose_name="activo")

    def __str__(self):
        fila = self.apellido + ", " + self.nombre
        return fila

class Cobrador(models.Model):
    """Modelo Cobradores"""

    nombre = models.CharField(max_length=45, verbose_name="nombre")

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True, verbose_name="activo")

    def __str__(self):
        return self.nombre

class Abono(models.Model):
    """Modelo Abonos"""
    cliente = models.ForeignKey(
        'Cliente',
        blank=True,
        null=True,
        on_delete=SET_NULL
        )
    cobrador = models.ForeignKey(
        'Cobrador',
        blank=True,
        null=True,
        on_delete=SET_NULL
        )
    
    fecha = models.DateField(
        blank=True,
        null=True,
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

    def __str__(self):
        fila = str(self.fecha) + ", " + str(self.monto) + ", " + self.cobrador.nombre
        return fila

class Recaudacion(models.Model):
    """Modelo Recaudación"""

    cobrador = models.ForeignKey(
        'Cobrador',
        blank=False,
        null=True,
        on_delete=SET_NULL
        )
    
    fecha = models.DateField(
        blank=True,
        null=True,
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

    def __str__(self):
        fila = self.cobrador.nombre + ", " + str(self.fecha) + ", " + str(self.monto)
        return fila