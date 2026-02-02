"""
============================================================
Módulo: datos.py
============================================================
Descripción: Contiene las estructuras de datos iniciales
del sistema. Utiliza diccionarios, listas, tuplas
y conjuntos según corresponda.
============================================================
"""

# -------------------------------------------------------------
# DICCIONARIO PRINCIPAL: Inventario de productos
# Estructura: {ID: {nombre, precio, stock, categoria, proveedor}}
# Uso: Almacenamiento principal de datos (clave-valor)
# -------------------------------------------------------------
inventario = {
    "P001": {
        "nombre": "Laptop Dell XPS",
        "precio": 1250000.00,
        "stock": 8,
        "categoria": "Electrónica",
        "proveedor": "TechDistributor"
    },
    "P002": {
        "nombre": "Mouse Logitech MX3",
        "precio": 18500.00,
        "stock": 45,
        "categoria": "Accesorios",
        "proveedor": "OfficeSupply"
    },
    "P003": {
        "nombre": "Teclado Mecánico Razer",
        "precio": 52000.00,
        "stock": 3,
        "categoria": "Accesorios",
        "proveedor": "TechDistributor"
    },
    "P004": {
        "nombre": "Monitor Samsung 27\"",
        "precio": 380000.00,
        "stock": 12,
        "categoria": "Electrónica",
        "proveedor": "SamsungOfficial"
    },
    "P005": {
        "nombre": "Auriculares Sony WH-1000",
        "precio": 95000.00,
        "stock": 2,
        "categoria": "Audio",
        "proveedor": "SonyStore"
    },
    "P006": {
        "nombre": "Cámara Web Logitech C920",
        "precio": 42000.00,
        "stock": 15,
        "categoria": "Accesorios",
        "proveedor": "OfficeSupply"
    },
    "P007": {
        "nombre": "Disco Duro Externo 2TB",
        "precio": 8900.00,
        "stock": 0,
        "categoria": "Almacenamiento",
        "proveedor": "TechDistributor"
    }
}

# -------------------------------------------------------------
# CONJUNTO (set): Categorías válidas del sistema
# Uso: Garantizar unicidad y validar categorías
# Operaciones: intersección, unión, diferencia
# -------------------------------------------------------------
categorias_validas = {
    "Electrónica",
    "Accesorios",
    "Audio",
    "Almacenamiento",
    "Software",
    "Networking"
}

# -------------------------------------------------------------
# TUPLA: Proveedores autorizados (datos inmutables)
# Uso: Lista fija de proveedores que no debe cambiar
# -------------------------------------------------------------
proveedores = (
    "TechDistributor",
    "OfficeSupply",
    "SamsungOfficial",
    "SonyStore",
    "AppleStore",
    "OfficialHP"
)

# -------------------------------------------------------------
# TUPLA: Configuración del sistema (inmutable)
# Uso: Parámetros fijos del sistema
# -------------------------------------------------------------
configuracion_sistema = (
    ("stock_minimo", 5),           # Umbral de stock bajo
    ("precio_minimo", 100.00),     # Precio mínimo permitido
    ("precio_maximo", 5000000.00), # Precio máximo permitido
    ("max_productos", 500)         # Máximo de productos permitidos
)


def obtener_config(clave):
    """
    Función recursiva que busca un valor de configuración
    por su clave dentro de la tupla de configuración.

    Parámetros:
        clave (str): La clave a buscar
    Retorna:
        valor: El valor asociado a la clave o None
    """
    def buscar_recursivo(configs, indice):
        # Caso base: llegamos al final sin encontrar
        if indice >= len(configs):
            return None
        # Caso base: encontramos la clave
        if configs[indice][0] == clave:
            return configs[indice][1]
        # Caso recursivo: buscar en el siguiente elemento
        return buscar_recursivo(configs, indice + 1)

    return buscar_recursivo(configuracion_sistema, 0)