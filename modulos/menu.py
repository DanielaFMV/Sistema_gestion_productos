"""
============================================================
Módulo: menu.py
============================================================
Descripción: Funciones para mostrar el menú principal
y sub-menús del sistema de gestión.
============================================================
"""


def mostrar_menu_principal():
    """
    Muestra el menú principal del sistema con todas
    las opciones disponibles formateadas con f-strings.
    """
    print("\n" + "=" * 60)
    print("  📋 MENÚ PRINCIPAL - Sistema de Gestión de Productos")
    print("=" * 60)
    print("  1️⃣  Listar todos los productos")
    print("  2️⃣  Agregar nuevo producto")
    print("  3️⃣  Buscar producto")
    print("  4️⃣  Actualizar producto")
    print("  5️⃣  Eliminar producto")
    print("  ─" * 30)
    print("  📊 REPORTES")
    print("  6️⃣  Reporte por categoría")
    print("  7️⃣  Reporte de stock bajo")
    print("  8️⃣  Reporte de valor del inventario")
    print("  ─" * 30)
    print("  9️⃣  Salir del sistema")
    print("=" * 60)