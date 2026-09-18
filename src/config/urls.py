from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Rutas de la App 'biblioteca' (Parte 1 del Laboratorio 3)
    path('', include('biblioteca.urls')),
    
    # Rutas de la App 'empresa' (Parte 2 del Laboratorio 3)
    path('empresa/', include('empresa.urls')),
]