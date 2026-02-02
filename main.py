"""
============================================================
Sistema de Gestión de Productos
============================================================
Autor: [Daniela Muñoz]
Fecha: [02/02/2026]
Descripción: Sistema de gestión de productos para una
empresa de tecnología. Permite registrar, buscar,
actualizar y eliminar productos, además de
generar reportes y estadísticas.
============================================================
"""

# Importación de módulos del proyecto
from modulos.datos import inventario, categorias_validas, proveedores
from modulos.menu import mostrar_menu_principal
from modulos.operaciones import (
    agregar_producto,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    listar_productos
)
from modulos.reportes import (
    reporte_por_categoria,
    reporte_stock_bajo,
    reporte_valor_inventario,
    reporte_productos_unicos
)
from modulos.validaciones import validar_opcion_menu


def ejecutar_sistema():
    """
    Función principal que ejecuta el sistema de gestión.
    Implementa un menú iterativo usando while True con break.
    """
    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("  Empresa de Tecnología - Automatización Interna")
    print("=" * 60)

    while True:
        # Mostrar menú y capturar opción
        mostrar_menu_principal()
        opcion = input("\n  Seleccione una opción: ").strip()

        # Validar que la opción sea un número válido
        if not validar_opcion_menu(opcion, 1, 9):
            print("\n  ⚠️  Opción no válida. Ingrese un número del 1 al 9.")
            continue

        opcion = int(opcion)

        # Estructura tipo switch con diccionario
        acciones = {
            1: lambda: listar_productos(inventario),
            2: lambda: agregar_producto(inventario, categorias_validas, proveedores),
            3: lambda: buscar_producto(inventario),
            4: lambda: actualizar_producto(inventario),
            5: lambda: eliminar_producto(inventario),
            6: lambda: reporte_por_categoria(inventario),
            7: lambda: reporte_stock_bajo(inventario),
            8: lambda: reporte_valor_inventario(inventario),
        }

        if opcion == 9:
            # Salida del sistema con break
            print("\n  ✅ Gracias por usar el Sistema de Gestión de Productos.")
            print("  ✅ ¡Hasta luego!\n")
            break

        # Ejecutar la acción correspondiente usando get()
        accion = acciones.get(opcion)
        if accion:
            print("\n" + "-" * 60)
            accion()
            print("-" * 60)

        # Pausa antes de volver al menú
        input("\n  Presione Enter para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_sistema()