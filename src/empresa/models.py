from django.db import models

# 1. Categoria (Independiente)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# 2. Proveedor (Independiente)
class Proveedor(models.Model):
    ruc = models.CharField(max_length=11, unique=True)
    razon_social = models.CharField(max_length=150)

    def __str__(self):
        return self.razon_social

# 3. Cliente (Independiente)
class Cliente(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.dni})"

# 4. PerfilCliente (Relación 1:1 con Cliente)
class PerfilCliente(models.Model):
    cliente = models.OneToOneField(
        Cliente, 
        on_delete=models.CASCADE, 
        related_name="perfil"
    )
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"Perfil de {self.cliente.nombre}"

# 5. Producto (Relación 1:N con Categoria)
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.PROTECT, 
        related_name="productos"
    )

    def __str__(self):
        return self.nombre

# 6. Venta (Entidad de Transacción)
class Venta(models.Model):
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT, 
        related_name="ventas"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(
        Producto, 
        through="DetalleVenta", 
        related_name="ventas"
    )

    def __str__(self):
        return f"Venta #{self.id} - {self.cliente.nombre}"

# 7. DetalleVenta (Modelo Intermedio N:M con atributos propios)
class DetalleVenta(models.Model):
    venta = models.ForeignKey(
        Venta, 
        on_delete=models.CASCADE, 
        related_name="detalles"
    )
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.PROTECT, 
        related_name="detalles_venta"
    )
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre} en Venta #{self.venta.id}"