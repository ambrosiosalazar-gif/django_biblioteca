from django.contrib import admin
from .models import (
    Categoria,
    Proveedor,
    Cliente,
    PerfilCliente,
    Producto,
    Venta,
    DetalleVenta
)

# Inline 1:1 con StackedInline (Ejercicio 11)
class PerfilClienteInline(admin.StackedInline):
    model = PerfilCliente
    can_delete = False
    verbose_name_plural = 'Perfil de Cliente'

# Personalización de Cliente con el StackedInline embebido
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'dni')
    search_fields = ('nombre', 'dni')
    inlines = [PerfilClienteInline]

# Inline N:M para Ventas
class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha')
    inlines = [DetalleVentaInline]

# Personalización para Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria')
    search_fields = ('nombre',)
    list_filter = ('categoria',)

# Personalización para Proveedor
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'razon_social', 'ruc')
    search_fields = ('razon_social', 'ruc')

# Registro de modelos en el Admin
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)

# Registros estándar
admin.site.register(Categoria)
admin.site.register(PerfilCliente)
admin.site.register(DetalleVenta)