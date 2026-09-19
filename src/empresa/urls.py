from django.urls import path
from . import views

urlpatterns = [
    # Rutas CRUD Productos
    path('', views.lista_productos_empresa, name='lista_productos_empresa'),
    path('crear/', views.crear_producto_empresa, name='crear_producto_empresa'),
    path('editar/<int:id>/', views.editar_producto_empresa, name='editar_producto_empresa'),
    path('eliminar/<int:id>/', views.eliminar_producto_empresa, name='eliminar_producto_empresa'),
    
    # Rutas Modelo Intermedio (DetalleVenta)
    path('venta/<int:venta_id>/', views.detalle_venta_view, name='detalle_venta'),
    path('venta/<int:venta_id>/agregar/', views.crear_detalle_venta, name='crear_detalle_venta'),
    path('detalle/editar/<int:id>/', views.editar_detalle_venta, name='editar_detalle_venta'),
    path('detalle/eliminar/<int:id>/', views.eliminar_detalle_venta, name='eliminar_detalle_venta'),
]