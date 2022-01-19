from django.contrib import admin
from .models import Cliente, Cobrador, Abono, Recaudacion

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Cobrador)
admin.site.register(Abono)
admin.site.register(Recaudacion)