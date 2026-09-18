from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria

# 15. READ - Listar Productos
def lista_productos_empresa(request):
    productos = Producto.objects.all().order_by('-id')
    return render(request, 'empresa/lista_productos.html', {'productos': productos})

# 14. CREATE - Crear Producto con Categoria (ForeignKey)
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

# 16. UPDATE - Editar Producto
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

# 17. DELETE - Eliminar Producto con Confirmación
def eliminar_producto_empresa(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos_empresa')
    return render(request, 'empresa/confirmar_eliminar.html', {'producto': producto})