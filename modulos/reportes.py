"""
============================================================
Módulo: reportes.py
============================================================
Descripción: Funciones para generar reportes y
estadísticas del inventario. Aplica listas,
conjuntos, tuplas y comprensiones.
============================================================
"""

from modulos.datos import obtener_config


def reporte_por_categoria(inventario):
    """
    Genera un reporte agrupando productos por categoría.
    Utiliza diccionarios y sets para organizar datos.

    Parámetros:
        inventario (dict): Diccionario de productos
    """
    if not inventario:
        print("\n  ❌ No hay productos para generar reporte.")
        return

    print("\n  📊 REPORTE POR CATEGORÍA")

    # Crear diccionario agrupado por categoría
    categorias = {}
    for codigo, datos in inventario.items():
        cat = datos["categoria"]
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append((codigo, datos))

    # Mostrar reporte usando for y condicionales
    for categoria, productos in categorias.items():
        total_productos = len(productos)
        total_stock = sum(p[1]["stock"] for p in productos)
        valor_total = sum(p[1]["precio"] * p[1]["stock"] for p in productos)

        print(f"\n  📁 {categoria}")
        print(f"  {'─' * 50}")
        print(f"  Cantidad de productos: {total_productos}")
        print(f"  Stock total:           {total_stock} unidades")
        print(f"  Valor total:           ${valor_total:,.2f}")
        print(f"  Productos:")

        for codigo, datos in productos:
            print(f"    • [{codigo}] {datos['nombre']} - Stock: {datos['stock']}")


def reporte_stock_bajo(inventario):
    """
    Muestra productos con stock por debajo del mínimo
    o sin stock. Utiliza condicionales y lists.

    Parámetros:
        inventario (dict): Diccionario de productos
    """
    print("\n  ⚠️  REPORTE DE STOCK BAJO")
    stock_minimo = obtener_config("stock_minimo")

    # Lista de productos sin stock
    sin_stock = []
    # Lista de productos con stock bajo
    stock_bajo = []

    # Clasificar productos usando for y condicionales
    for codigo, datos in inventario.items():
        if datos["stock"] == 0:
            sin_stock.append((codigo, datos))
        elif datos["stock"] < stock_minimo:
            stock_bajo.append((codigo, datos))

    # Mostrar productos sin stock
    if sin_stock:
        print(f"\n  🚨 PRODUCTOS SIN STOCK ({len(sin_stock)}):")
        print(f"  {'─' * 50}")
        for codigo, datos in sin_stock:
            print(f"  ❌ [{codigo}] {datos['nombre']}")
            print(f"      Categoría: {datos['categoria']} | Proveedor: {datos['proveedor']}")
    else:
        print("\n  ✅ Todos los productos tienen stock disponible.")

    # Mostrar productos con stock bajo
    if stock_bajo:
        print(f"\n  ⚠️  PRODUCTOS CON STOCK BAJO (< {stock_minimo} unidades) ({len(stock_bajo)}):")
        print(f"  {'─' * 50}")
        for codigo, datos in stock_bajo:
            print(f"  📦 [{codigo}] {datos['nombre']}")
            print(f"      Stock actual: {datos['stock']} | Precio: ${datos['precio']:,.2f}")
    else:
        print(f"\n  ✅ Todos los productos tienen stock >= {stock_minimo} unidades.")

    # Si no hay problemas de stock
    if not sin_stock and not stock_bajo:
        print("\n  🎉 El inventario está en excelente estado.")


def reporte_valor_inventario(inventario):
    """
    Calcula y muestra estadísticas del valor total
    del inventario. Usa funciones matemáticas y
    comprensiones de listas.

    Parámetros:
        inventario (dict): Diccionario de productos
    """
    print("\n  💰 REPORTE DE VALOR DEL INVENTARIO")

    if not inventario:
        print("\n  ❌ No hay productos en el inventario.")
        return

    # Crear lista de tuplas con (nombre, precio, stock, valor_total)
    datos_productos = [
        (datos["nombre"], datos["precio"], datos["stock"],
         datos["precio"] * datos["stock"])
        for datos in inventario.values()
    ]

    # Calcular estadísticas
    valor_total = sum(producto[3] for producto in datos_productos)
    precio_promedio = sum(producto[1] for producto in datos_productos) / len(datos_productos)
    stock_total = sum(producto[2] for producto in datos_productos)

    # Encontrar producto más expensive y más barato
    producto_mas_caro = max(datos_productos, key=lambda x: x[1])
    producto_mas_barato = min(datos_productos, key=lambda x: x[1])
    producto_mayor_valor = max(datos_productos, key=lambda x: x[3])

    # Mostrar reporte
    print(f"\n  {'─' * 50}")
    print(f"  📊 Estadísticas Generales:")
    print(f"  {'─' * 50}")
    print(f"  Total de productos:      {len(inventario)}")
    print(f"  Stock total:             {stock_total} unidades")
    print(f"  Valor total inventario:  ${valor_total:,.2f}")
    print(f"  Precio promedio:         ${precio_promedio:,.2f}")

    print(f"\n  📈 Productos Destacados:")
    print(f"  {'─' * 50}")
    print(f"  💎 Más expensive:   {producto_mas_caro[0]} (${producto_mas_caro[1]:,.2f})")
    print(f"  💚 Más barato:      {producto_mas_barato[0]} (${producto_mas_barato[1]:,.2f})")
    print(f"  🏆 Mayor valor:     {producto_mayor_valor[0]} (${producto_mayor_valor[3]:,.2f})")

    # Tabla detallada
    print(f"\n  📋 Detalle por producto:")
    print(f"  {'─' * 50}")
    print(f"  {'Producto':<30} {'Precio':>10} {'Stock':>6} {'Valor':>12}")
    print(f"  {'-'*30} {'-'*10} {'-'*6} {'-'*12}")

    for nombre, precio, stock, valor in datos_productos:
        print(f"  {nombre:<30} ${precio:>9,.2f} {stock:>6} ${valor:>11,.2f}")

    print(f"  {'-'*30} {'-'*10} {'-'*6} {'-'*12}")
    print(f"  {'TOTAL':<30} {'':>10} {stock_total:>6} ${valor_total:>11,.2f}")


def reporte_productos_unicos(inventario):
    """
    Muestra categorías y proveedores únicos usando sets.
    Demonstra operaciones de conjuntos.

    Parámetros:
        inventario (dict): Diccionario de productos
    """
    print("\n  🔍 REPORTE DE DATOS ÚNICOS")

    # Crear sets de categorías y proveedores únicos
    categorias_unicas = set()
    proveedores_unicos = set()

    for datos in inventario.values():
        categorias_unicas.add(datos["categoria"])
        proveedores_unicos.add(datos["proveedor"])

    print(f"\n  📁 Categorías únicas ({len(categorias_unicas)}):")
    for cat in sorted(categorias_unicas):
        print(f"    • {cat}")

    print(f"\n  🏢 Proveedores únicos ({len(proveedores_unicos)}):")
    for prov in sorted(proveedores_unicos):
        print(f"    • {prov}")

    # Demostrar operaciones de conjuntos
    print(f"\n  🔄 Operaciones de conjuntos:")
    print(f"    • Unión categorías + proveedores: {len(categorias_unicas | proveedores_unicos)} elementos")
    print(f"    • Intersección: {categorias_unicas & proveedores_unicos or 'Ningún elemento en común'}")