from django.db import models

# 1:N - Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Entidad Principal
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.PROTECT, 
        related_name="productos",
        null=True, blank=True
    )

    def __str__(self):
        return self.nombre

# 1:1 - Ficha complementaria del Producto
class DetalleTecnico(models.Model):
    producto = models.OneToOneField(
        Producto, 
        on_delete=models.CASCADE, 
        related_name="detalle_tecnico"
    )
    especificaciones = models.TextField()
    garantia_meses = models.IntegerField(default=12)

    def __str__(self):
        return f"Detalle de {self.producto.nombre}"

# N:M - Proveedor y Modelo Intermedio Suministro
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    productos = models.ManyToManyField(
        Producto, 
        through="Suministro", 
        related_name="proveedores"
    )

    def __str__(self):
        return self.nombre

class Suministro(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_suministro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.proveedor.nombre} -> {self.producto.nombre}"