# Django Laboratory - App Empresa (GLAB-S05)

Este proyecto implementa la gestión administrativa de la aplicación `empresa` utilizando el panel de administración de Django (`django.contrib.admin`).

## Modelos Registrados
Se configuraron un total de 7 modelos en la interfaz de administración:
1. **Categoria**: Gestión de categorías de productos.
2. **Proveedor**: Gestión de datos comerciales de proveedores.
3. **Cliente**: Datos principales del cliente (DNI, Nombre).
4. **PerfilCliente**: Información complementaria (Teléfono, Dirección) vinculada 1:1 con `Cliente`.
5. **Producto**: Catálogo de productos con precio, stock y categoría.
6. **Venta**: Registro de transacciones asociadas a clientes.
7. **DetalleVenta**: Modelo intermedio N:M entre `Venta` y `Producto` con cantidad y precio unitario.

## Personalizaciones de `ModelAdmin`
- **`ProductoAdmin`**: Implementa `list_display` (id, nombre, precio, stock, categoria), `search_fields` (nombre) y `list_filter` (categoria).
- **`ClienteAdmin`**: Configurado con `list_display` (id, nombre, dni), `search_fields` (nombre, dni) e incluye el `PerfilClienteInline` (`StackedInline`).
- **`ProveedorAdmin`**: Configurado con `list_display` (id, razon_social, ruc) y `search_fields` (razon_social, ruc).
- **`VentaAdmin`**: Muestra `list_display` (id, cliente, fecha) e integra `DetalleVentaInline` (`TabularInline`) para gestionar ítems y atributos propios de la relación N:M.

## Instrucciones de Ejecución
1. Activar entorno virtual: `.\venv\Scripts\activate`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar servidor: `python manage.py runserver`