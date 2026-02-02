"""
============================================================
Módulo: validaciones.py
============================================================
Descripción: Funciones de validación para entradas del
usuario. Garantiza la integridad de datos antes
de procesarlos en el sistema.
============================================================
"""

from modulos.datos import obtener_config


def validar_opcion_menu(opcion, min_val, max_val):
    """
    Valida que la opción del menú sea un número entero
    dentro del rango permitido.

    Parámetros:
        opcion (str): Valor ingresado por el usuario
        min_val (int): Valor mínimo permitido
        max_val (int): Valor máximo permitido
    Retorna:
        bool: True si es válido, False en caso contrario
    """
    try:
        valor = int(opcion)
        return min_val <= valor <= max_val
    except ValueError:
        return False


def validar_nombre_producto(nombre):
    """
    Valida que el nombre del producto sea una cadena
    no vacía con al menos 3 caracteres.

    Parámetros:
        nombre (str): Nombre del producto a validar
    Retorna:
        bool: True si es válido, False en caso contrario
    """
    if not nombre or len(nombre.strip()) < 3:
        return False
    # Verificar que no contenga solo números
    if nombre.strip().isdigit():
        return False
    return True


def validar_precio(precio_str):
    """
    Valida que el precio sea un número positivo dentro
    del rango permitido por la configuración del sistema.

    Parámetros:
        precio_str (str): Precio ingresado como texto
    Retorna:
        tuple: (es_valido, precio_float o mensaje_error)
    """
    precio_min = obtener_config("precio_minimo")
    precio_max = obtener_config("precio_maximo")

    try:
        precio = float(precio_str)
        if precio <= 0:
            return (False, "El precio debe ser mayor a 0.")
        if precio < precio_min:
            return (False, f"El precio mínimo permitido es ${precio_min:.2f}")
        if precio > precio_max:
            return (False, f"El precio máximo permitido es ${precio_max:.2f}")
        return (True, precio)
    except ValueError:
        return (False, "El precio debe ser un número válido.")


def validar_stock(stock_str):
    """
    Valida que el stock sea un número entero no negativo.

    Parámetros:
        stock_str (str): Stock ingresado como texto
    Retorna:
        tuple: (es_valido, stock_int o mensaje_error)
    """
    try:
        stock = int(stock_str)
        if stock < 0:
            return (False, "El stock no puede ser negativo.")
        return (True, stock)
    except ValueError:
        return (False, "El stock debe ser un número entero.")


def validar_categoria(categoria, categorias_validas):
    """
    Valida que la categoría ingresada pertenezca al
    conjunto de categorías válidas del sistema.

    Parámetros:
        categoria (str): Categoría a validar
        categorias_validas (set): Conjunto de categorías permitidas
    Retorna:
        bool: True si es válida, False en caso contrario
    """
    return categoria.strip() in categorias_validas


def validar_proveedor(proveedor, proveedores):
    """
    Valida que el proveedor ingresado esté en la tupla
    de proveedores autorizados.

    Parámetros:
        proveedor (str): Proveedor a validar
        proveedores (tuple): Tupla de proveedores autorizados
    Retorna:
        bool: True si es válido, False en caso contrario
    """
    return proveedor.strip() in proveedores


def validar_codigo_producto(codigo):
    """
    Valida el formato del código de producto.
    Debe ser formato 'P' seguido de 3 dígitos (Ej: P001).

    Parámetros:
        codigo (str): Código a validar
    Retorna:
        bool: True si el formato es correcto
    """
    if len(codigo) != 4:
        return False
    if codigo[0] != 'P':
        return False
    if not codigo[1:].isdigit():
        return False
    return True