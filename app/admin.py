from django.contrib import admin
from .models import Cargo, DetalleVale, Empleado, Perfil, Servicio, Sucursal, Turno, Vale, Venta

# Register your models here.
admin.site.register(Cargo)
admin.site.register(DetalleVale)
admin.site.register(Empleado)
admin.site.register(Perfil)
admin.site.register(Servicio)
admin.site.register(Sucursal)
admin.site.register(Turno)
admin.site.register(Vale)
admin.site.register(Venta)