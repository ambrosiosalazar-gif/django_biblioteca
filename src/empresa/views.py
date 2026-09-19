from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Venta, DetalleVenta

# --- CRUD PRODUCTO ---
def lista_productos_empresa(request):
    productos = Producto.objects.select_related('categoria').all().order_by('-id')
    return render(request, 'empresa/lista_productos.html', {'productos': productos})

def crear_producto_empresa(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria_id = request.POST.get('categoria')
        
        categoria = get_object_or_404(Categoria, id=categoria_id)
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            stock=stock,
            categoria=categoria
        )
        return redirect('lista_productos_empresa')
        
    categorias = Categoria.objects.all()
    return render(request, 'empresa/crear_producto.html', {'categorias': categorias})

def editar_producto_empresa(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        categoria_id = request.POST.get('categoria')
        
        producto.categoria = get_object_or_404(Categoria, id=categoria_id)
        producto.save()
        return redirect('lista_productos_empresa')
        
    categorias = Categoria.objects.all()
    return render(request, 'empresa/editar_producto.html', {'producto': producto, 'categorias': categorias})

def eliminar_producto_empresa(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos_empresa')
    return render(request, 'empresa/confirmar_eliminar.html', {'producto': producto})

# --- CONSULTA Y CRUD MODELO INTERMEDIO (DetalleVenta) ---
def detalle_venta_view(request, venta_id):
    venta = get_object_or_404(
        Venta.objects
        .select_related('cliente', 'cliente__perfil')
        .prefetch_related('detalles__producto'),
        id=venta_id
    )
    return render(request, 'empresa/detalle_venta.html', {'venta': venta})

def crear_detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')
        precio_unitario = request.POST.get('precio_unitario')
        
        producto = get_object_or_404(Producto, id=producto_id)
        DetalleVenta.objects.create(
            venta=venta,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=precio_unitario
        )
        return redirect('detalle_venta', venta_id=venta.id)
        
    productos = Producto.objects.all()
    return render(request, 'empresa/crear_detalle.html', {'venta': venta, 'productos': productos})

def editar_detalle_venta(request, id):
    detalle = get_object_or_404(DetalleVenta, id=id)
    if request.method == 'POST':
        detalle.cantidad = request.POST.get('cantidad')
        detalle.precio_unitario = request.POST.get('precio_unitario')
        detalle.save()
        return redirect('detalle_venta', venta_id=detalle.venta.id)
    return render(request, 'empresa/editar_detalle.html', {'detalle': detalle})

def eliminar_detalle_venta(request, id):
    detalle = get_object_or_404(DetalleVenta, id=id)
    venta_id = detalle.venta.id
    if request.method == 'POST':
        detalle.delete()
        return redirect('detalle_venta', venta_id=venta_id)
    return render(request, 'empresa/confirmar_eliminar_detalle.html', {'detalle': detalle})