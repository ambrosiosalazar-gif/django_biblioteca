from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos_empresa, name='lista_productos_empresa'),
    path('crear/', views.crear_producto_empresa, name='crear_producto_empresa'),
    path('editar/<int:id>/', views.editar_producto_empresa, name='editar_producto_empresa'),
    path('eliminar/<int:id>/', views.eliminar_producto_empresa, name='eliminar_producto_empresa'),
]