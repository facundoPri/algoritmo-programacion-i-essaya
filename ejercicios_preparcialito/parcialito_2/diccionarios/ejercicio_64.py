"""
Se tiene un diccionario de la forma {nombre_vendedor : total_vendido}, con la suma total de lo vendido por distintos vendedores, y otro con forma {local : [nombre_vendedor_1, nombre_vendedor_2, …]}, con los vendedores que trabajan en cada local. Escribir una función que reciba diccionarios como los mencionados, y devuelva un nuevo diccionario cuyas claves sean los nombres de los locales y sus valores el total vendido por los vendedores de ese local.
"""
vendedores = {
    "jose": 1000,
    "juan": 500,
    "jorge": 750,
    "jaime": 800,
    "juaquin": 500,
    "jacinto": 2000,
}

locales = {
    "chino de la esquina": ["jose", "juan", "jorge"],
    "chino de la otra esquina": ["jaime"],
    "chino de la tercer esquina": ["juaquin", "jacinto"],
}


def calcular_total_local(vendedores, locales):
    """
    Recibe dos diccionarios uno con los vendedores y la suma de lo vendido por ellos y otro que son donde trabajan los vendedores
    Devuelv un diccionario con la suma total de ventas de cada local
    """
    ventas_por_local = {}
    for local, vendedores_local in locales.items():
        ventas_por_local[local] = 0
        for vendedor in vendedores_local:
            ventas_por_local[local] += vendedores.get(vendedor, 0)
    return ventas_por_local


print(calcular_total_local(vendedores, locales))
