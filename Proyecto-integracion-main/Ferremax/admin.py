from django.contrib import admin
from .models import categoria, marca, proveedor, producto, cargo, empleado
# Register your models here.

admin.site.register(categoria) 
admin.site.register(marca) 
admin.site.register(proveedor) 
admin.site.register(producto)
admin.site.register(cargo)
admin.site.register(empleado)
