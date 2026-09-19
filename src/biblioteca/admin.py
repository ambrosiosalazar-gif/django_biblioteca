from django.contrib import admin
from .models import Categoria, Producto, DetalleTecnico, Proveedor, Suministro

class DetalleTecnicoInline(admin.StackedInline):
    model = DetalleTecnico
    extra = 0

class SuministroInline(admin.TabularInline):
    model = Suministro
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria')
    search_fields = ('nombre',)
    list_filter = ('categoria',)
    inlines = [DetalleTecnicoInline, SuministroInline]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)