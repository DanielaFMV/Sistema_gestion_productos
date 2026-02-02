# 🐍 Sistema de Gestión de Productos

## 📋 Descripción
Sistema de gestión de productos desarrollado en Python para una empresa de tecnología. Permite registrar, buscar, actualizar y eliminar productos del inventario, además de generar reportes y estadísticas detalladas.

---

## 🏗️ Estructura del Proyecto

```
proyecto_gestion_productos/
│
├── main.py                    # Punto de entrada principal
├── modulos/
│   ├── __init__.py            # Inicialización del paquete
│   ├── datos.py               # Estructuras de datos iniciales
│   ├── validaciones.py        # Funciones de validación de entrada
│   ├── operaciones.py         # Operaciones CRUD del sistema
│   ├── reportes.py            # Reportes y estadísticas
│   └── menu.py                # Menú interactivo
├── datos_entrada.csv          # Archivo de prueba con datos
└── README.md                  # Este archivo
```

---

## 🎯 Funcionalidades

### Gestión de Productos
- ✅ Listar todos los productos con formato visual
- ✅ Agregar nuevos productos con validación completa
- ✅ Buscar productos por código o nombre
- ✅ Actualizar información de productos existentes
- ✅ Eliminar productos con confirmación

### Reportes
- 📊 Reporte agrupado por categoría
- ⚠️ Reporte de stock bajo y productos agotados
- 💰 Reporte de valor total del inventario con estadísticas

---

## 🧱 Estructuras de Datos Utilizadas

| Estructura | Ubicación | Uso en el proyecto |
|-----------|-----------|-------------------|
| **Diccionario (dict)** | datos.py, operaciones.py | Almacenamiento principal de productos (clave-valor) |
| **Conjunto (set)** | datos.py, reportes.py | Categorías válidas, eliminación de duplicados |
| **Tupla (tuple)** | datos.py | Proveedores autorizados (datos inmutables), configuración del sistema |
| **Lista (list)** | operaciones.py, reportes.py | Resultados de búsqueda, clasificación de productos |

---

## ⚙️ Conceptos Aplicados

### Estructuras de Control
- `if`, `elif`, `else` para decisiones y validaciones
- `for` para iterar sobre diccionarios y listas
- `while True` para el menú interactivo
- `break` para salir del bucle principal
- `continue` para reiniciar el menú al haber errores

### Funciones
- Funciones personalizadas con parámetros y retorno (`return`)
- Función recursiva: `obtener_config()` en datos.py
- Funciones lambda: usadas en reportes con `max()` y `min()`
- Procedimientos (funciones sin retorno): funciones de visualización

### Modularización
- Código organizado en 5 módulos separados
- Uso de `import` para reutilizar funciones entre archivos
- Paquete con `__init__.py`
- Estructura tipo switch usando diccionarios

### Validaciones
- Entrada de datos validada en todos los campos
- Manejo de errores con try/except
- Validación de tipos de datos (int, float, str)
- Rango de valores configurables

---

## 🚀 Cómo Ejecutar

1. Abre la carpeta `proyecto_gestion_productos` en tu terminal
2. Ejecuta el archivo principal:
```bash
python main.py
```
3. Sigue las opciones del menú interactivo

---

## 📝 Ejemplo de Uso

```
============================================================
  SISTEMA DE GESTIÓN DE PRODUCTOS
  Empresa de Tecnología - Automatización Interna
============================================================

  📋 MENÚ PRINCIPAL
  1️⃣  Listar todos los productos
  2️⃣  Agregar nuevo producto
  3️⃣  Buscar producto
  ...
  9️⃣  Salir del sistema

  Seleccione una opción: 1

  📦 LISTA DE PRODUCTOS DEL INVENTARIO
  Código   Nombre                         Precio       Stock Categoría
  P001     Laptop Dell XPS          $1,250,000.00     8     Electrónica
  ...
```

---

## 📚 referencias
- [PEP 8 - Guía de estilo Python](https://peps.python.org/pep-0008/)
- [Python Data Structures - Real Python](https://realpython.com/python-data-structures/)
- [Python Modules - Real Python](https://realpython.com/python-modules-packages/)
- [W3Schools Python](https://www.w3schools.com/python/)

---

## 🎓 Aprendizajes y Desafíos

### Desafíos enfrentados
- Organizar el código en múltiples módulos manteniendo la cohesión
- Implementar validaciones robustas para todos los campos
- Balancear la complejidad del sistema con la legibilidad del código

### Soluciones implementadas
- Uso de diccionarios anidados para representar productos de manera natural
- Funciones de validación modulares reutilizables en todo el sistema
- Estructura tipo switch con diccionarios para un menú limpio y escalable
- Función recursiva para búsqueda en configuración del sistema