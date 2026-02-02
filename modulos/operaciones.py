"""
============================================================
Módulo: operaciones.py
============================================================
Descripción: Funciones principales del sistema para
CRUD (Crear, Leer, Actualizar, Eliminar)
de productos en el inventario.
============================================================
"""

from modulos.validaciones import (
    validar_nombre_producto,
    validar_precio,
    validar_stock,
    validar_categoria,
    validar_proveedor,
    validar_codigo_producto
)
from modulos.datos import obtener_config


def generar_codigo(inventario):
    """
    Genera automáticamente el siguiente código de producto
    basándose en los códigos existentes en el inventario.

    Parámetros:
        inventario (dict): Diccionario actual de productos
    Retorna:
        str: Nuevo código de producto (Ej: P008)
    """
    if not inventario:
        return "P001"
    # Extraer números de los códigos existentes
    numeros = [int(codigo[1:]) for codigo in inventario.keys()]
    siguiente = max(numeros) + 1
    return f"P{siguiente:03d}"


def listar_productos(inventario):
    """
    Muestra todos los productos del inventario con
    formato legible usando f-strings.

    Parámetros:
        inventario (dict): Diccionario de productos
    """
    if not inventario:
        print("\n  ❌ No hay productos registrados en el sistema.")
        return

    print("\n  📦 LISTA DE PRODUCTOS DEL INVENTARIO")
    print(f"\n  {'Código':<8} {'Nombre':<30} {'Precio':>12} {'Stock':>6} {'Categoría':<15}")
    print(f"  {'-'*8} {'-'*30} {'-'*12} {'-'*6} {'-'*15}")

    # Recorrer diccionario con items() usando for
    for codigo, datos in inventario.items():
        nombre = datos["nombre"]
        precio = datos["precio"]
        stock = datos["stock"]
        categoria = datos["categoria"]

        # Indicador visual de stock bajo usando condicionales
        indicador = ""
        stock_minimo = obtener_config("stock_minimo")
        if stock == 0:
            indicador = " 🚨"  # Sin stock
        elif stock < stock_minimo:
            indicador = " ⚠️"   # Stock bajo

        print(f"  {codigo:<8} {nombre:<30} ${precio:>11,.2f} {stock:>5}{indicador} {categoria:<15}")

    print(f"\n  Total de productos: {len(inventario)}")


def agregar_producto(inventario, categorias_validas, proveedores):
    """
    Agrega un nuevo producto al inventario con
    validación completa de todos los campos.

    Parámetros:
        inventario (dict): Diccionario de productos
        categorias_validas (set): Categorías permitidas
        proveedores (tuple): Proveedores autorizados
    """
    print("\n  📝 AGREGAR NUEVO PRODUCTO")
    max_productos = obtener_config("max_productos")

    # Verificar límite de productos
    if len(inventario) >= max_productos:
        print(f"\n  ❌ Se ha alcanzado el máximo de {max_productos} productos.")
        return

    # --- Validar Nombre ---
    while True:
        nombre = input("\n  Ingrese nombre del producto: ").strip()
        if validar_nombre_producto(nombre):
            break
        print("  ⚠️  Nombre no válido. Debe tener al menos 3 caracteres.")

    # --- Validar Precio ---
    while True:
        precio_str = input("  Ingrese precio ($): ").strip()
        es_valido, resultado = validar_precio(precio_str)
        if es_valido:
            precio = resultado
            break
        print(f"  ⚠️  {resultado}")

    # --- Validar Stock ---
    while True:
        stock_str = input("  Ingrese cantidad de stock: ").strip()
        es_valido, resultado = validar_stock(stock_str)
        if es_valido:
            stock = resultado
            break
        print(f"  ⚠️  {resultado}")

    # --- Validar Categoría ---
    print(f"\n  Categorías disponibles: {', '.join(sorted(categorias_validas))}")
    while True:
        categoria = input("  Ingrese categoría: ").strip()
        if validar_categoria(categoria, categorias_validas):
            break
        print("  ⚠️  Categoría no válida. Seleccione una de la lista.")

    # --- Validar Proveedor ---
    print(f"\n  Proveedores autorizados: {', '.join(proveedores)}")
    while True:
        proveedor = input("  Ingrese proveedor: ").strip()
        if validar_proveedor(proveedor, proveedores):
            break
        print("  ⚠️  Proveedor no válido. Seleccione uno de la lista.")

    # Generar código automático
    nuevo_codigo = generar_codigo(inventario)

    # Crear el nuevo producto como diccionario
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "categoria": categoria,
        "proveedor": proveedor
    }

    # Agregar al inventario
    inventario[nuevo_codigo] = nuevo_producto

    print(f"\n  ✅ Producto agregado exitosamente!")
    print(f"  📌 Código asignado: {nuevo_codigo}")
    print(f"  📌 Producto: {nombre} | ${precio:,.2f} | Stock: {stock}")


def buscar_producto(inventario):
    """
    Busca productos por código o por nombre parcial.

    Parámetros:
        inventario (dict): Diccionario de productos
    """
    print("\n  🔍 BUSCAR PRODUCTO")
    print("  1. Buscar por código (Ej: P001)")
    print("  2. Buscar por nombre")

    opcion = input("\n  Seleccione opción (1/2): ").strip()

    if opcion == "1":
        codigo = input("  Ingrese código del producto: ").strip().upper()

        # Usar get() para evitar errores KeyError
        producto = inventario.get(codigo)
        if producto:
            print(f"\n  ✅ Producto encontrado:")
            print(f"  📌 Código:    {codigo}")
            print(f"  📌 Nombre:    {producto['nombre']}")
            print(f"  📌 Precio:    ${producto['precio']:,.2f}")
            print(f"  📌 Stock:     {producto['stock']}")
            print(f"  📌 Categoría: {producto['categoria']}")
            print(f"  📌 Proveedor: {producto['proveedor']}")
        else:
            print(f"\n  ❌ No se encontró producto con código '{codigo}'.")

    elif opcion == "2":
        nombre_buscar = input("  Ingrese nombre a buscar: ").strip().lower()

        # Filtrar productos que contienen el nombre buscado
        resultados = {
            codigo: datos for codigo, datos in inventario.items()
            if nombre_buscar in datos["nombre"].lower()
        }

        if resultados:
            print(f"\n  ✅ Se encontraron {len(resultados)} resultado(s):")
            for codigo, datos in resultados.items():
                print(f"\n  📌 [{codigo}] {datos['nombre']}")
                print(f"      Precio: ${datos['precio']:,.2f} | Stock: {datos['stock']}")
        else:
            print(f"\n  ❌ No se encontraron productos con '{nombre_buscar}'.")
    else:
        print("\n  ⚠️  Opción no válida.")


def actualizar_producto(inventario):
    """
    Actualiza información de un producto existente.
    Permite modificar nombre, precio, stock, categoría
    o proveedor individualmente.

    Parámetros:
        inventario (dict): Diccionario de productos
    """
    print("\n  ✏️  ACTUALIZAR PRODUCTO")
    codigo = input("  Ingrese código del producto a actualizar: ").strip().upper()

    producto = inventario.get(codigo)
    if not producto:
        print(f"\n  ❌ No se encontró producto con código '{codigo}'.")
        return

    print(f"\n  Producto actual: {producto['nombre']}")
    print("  ¿Qué desea actualizar?")
    print("  1. Nombre")
    print("  2. Precio")
    print("  3. Stock")
    print("  4. Categoría")
    print("  5. Proveedor")

    opcion = input("\n  Seleccione opción (1-5): ").strip()

    # Estructura condicional múltiple para cada campo
    if opcion == "1":
        nuevo_nombre = input("  Ingrese nuevo nombre: ").strip()
        if validar_nombre_producto(nuevo_nombre):
            producto["nombre"] = nuevo_nombre
            print(f"  ✅ Nombre actualizado a: {nuevo_nombre}")
        else:
            print("  ⚠️  Nombre no válido.")

    elif opcion == "2":
        nuevo_precio_str = input("  Ingrese nuevo precio ($): ").strip()
        es_valido, resultado = validar_precio(nuevo_precio_str)
        if es_valido:
            producto["precio"] = resultado
            print(f"  ✅ Precio actualizado a: ${resultado:,.2f}")
        else:
            print(f"  ⚠️  {resultado}")

    elif opcion == "3":
        nuevo_stock_str = input("  Ingrese nuevo stock: ").strip()
        es_valido, resultado = validar_stock(nuevo_stock_str)
        if es_valido:
            producto["stock"] = resultado
            print(f"  ✅ Stock actualizado a: {resultado}")
        else:
            print(f"  ⚠️  {resultado}")

    elif opcion == "4":
        from modulos.datos import categorias_validas
        print(f"  Categorías: {', '.join(sorted(categorias_validas))}")
        nueva_cat = input("  Ingrese nueva categoría: ").strip()
        if validar_categoria(nueva_cat, categorias_validas):
            producto["categoria"] = nueva_cat
            print(f"  ✅ Categoría actualizada a: {nueva_cat}")
        else:
            print("  ⚠️  Categoría no válida.")

    elif opcion == "5":
        from modulos.datos import proveedores
        print(f"  Proveedores: {', '.join(proveedores)}")
        nuevo_prov = input("  Ingrese nuevo proveedor: ").strip()
        if validar_proveedor(nuevo_prov, proveedores):
            producto["proveedor"] = nuevo_prov
            print(f"  ✅ Proveedor actualizado a: {nuevo_prov}")
        else:
            print("  ⚠️  Proveedor no válido.")
    else:
        print("  ⚠️  Opción no válida.")


def eliminar_producto(inventario):
    """
    Elimina un producto del inventario previa confirmación.

    Parámetros:
        inventario (dict): Diccionario de productos
    """
    print("\n  🗑️  ELIMINAR PRODUCTO")
    codigo = input("  Ingrese código del producto a eliminar: ").strip().upper()

    producto = inventario.get(codigo)
    if not producto:
        print(f"\n  ❌ No se encontró producto con código '{codigo}'.")
        return

    # Confirmación antes de eliminar
    print(f"\n  ⚠️  Producto a eliminar: {producto['nombre']}")
    confirmacion = input("  ¿Está seguro? (s/n): ").strip().lower()

    if confirmacion == "s":
        # Usar pop() para eliminar y obtener el valor
        producto_eliminado = inventario.pop(codigo)
        print(f"\n  ✅ Producto '{producto_eliminado['nombre']}' eliminado exitosamente.")
    else:
        print("\n  ❌ Operación cancelada.")