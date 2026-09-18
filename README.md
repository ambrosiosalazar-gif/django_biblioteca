# Laboratorio 3 - Sistema de Gestión de Inventario para Empresa Tecnológica

Este proyecto es una aplicación web desarrollada con **Django** que pasa de una arquitectura básica en memoria a una persistencia de datos relacional usando el ORM de Django y SQLite.

## 📌 Problemática
Las empresas de tecnología enfrentan dificultades al gestionar su inventario en hojas de cálculo o memoria temporal, lo que ocasiona pérdidas de stock, falta de trazabilidad en las ventas y errores al vincular proveedores y categorías de productos.

---

## 🎯 Requisitos Cumplidos

### Parte 1: Migración de `biblioteca`
- Implementación del modelo `Producto` utilizando el ORM de Django.
- Migraciones ejecutadas y verificadas en SQLite (`makemigrations` / `migrate`).
- Implementación de operaciones de lectura (READ) e inserción (CREATE).

### Parte 2: Solución Empresarial de 5 Entidades (`empresa`)
- **Modelos Creados:**
  1. `Categoria` (Independiente)
  2. `Proveedor` (Independiente)
  3. `Cliente` (Independiente)
  4. `Producto` (Relacionado con `Categoria` vía `ForeignKey`)
  5. `Venta` (Relacionado con `Cliente` vía `ForeignKey`)
- **Funcionalidades CRUD Implementadas:**
  - **Create (Crear):** Formulario para registrar nuevos productos asignando su categoría mediante `POST`.
  - **Read (Listar):** Consulta a la base de datos con `Producto.objects.all()` para desplegar el inventario.
  - **Update (Editar):** Formulario para actualizar información de un producto usando `save()`.
  - **Delete (Eliminar):** Eliminación de registros con pantalla de confirmación mediante `delete()`.
- **Patrón PRG:** Post/Redirect/Get implementado en la creación y edición para evitar duplicidad de envíos.

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.13
- **Framework:** Django 5.x
- **Base de Datos:** SQLite 3
- **Control de Versiones:** Git y GitHub