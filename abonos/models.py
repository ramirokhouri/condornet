"""Abonos models."""

# Django
from django.db import models
from django.db.models.deletion import DO_NOTHING

class Cliente(models.Model):
    """Modelo Clientes"""

    apellido = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return (self.apellido)

class Cobrador(models.Model):
    """Modelo Cobradores"""

    nombre = models.CharField(max_length=45)

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return (self.nombre)

class Abono(models.Model):
    """Modelo Abonos"""

    cliente = models.ForeignKey(
        'Cliente',
        blank=False,
        on_delete=DO_NOTHING,
        default=''
        )
    cobrador = models.ForeignKey(
        'Cobrador',
        blank=False,
        on_delete=DO_NOTHING,
        default=''
        )
    
    fecha = models.DateField(blank=True, null=True)
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
        )
    nota = models.CharField(max_length=100, blank=True)
    concepto = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return (self.monto)

class Recaudacion(models.Model):
    """Modelo Recaudación"""

    cobrador = models.ForeignKey(
        'Cobrador',
        blank=False,
        on_delete=DO_NOTHING,
        default=''
        )
    
    fecha = models.DateField(blank=True, null=True)
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
        )
    nota = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return (self.monto)