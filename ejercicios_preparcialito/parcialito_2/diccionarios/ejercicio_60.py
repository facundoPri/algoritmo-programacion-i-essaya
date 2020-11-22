"""
a. Escribir una función que dada una lista de tuplas, con el año en el que se disputó un mundial de fútbol y el equipo campeón de ese año, devuelva un diccionario con la cantidad de mundiales ganados por cada equipo. Un ejemplo de la lista de tuplas: [(1930, 'Uruguay'), (1934, 'Italia'), (1938, 'Italia'), ...]
b. Escribir otra función que reciba el diccionario generado en el punto anterior y devuelva una lista con el/los paises que ganaron más mundiales.
"""

copas_del_mundo = [
    (1930, "Uruguay"),
    (1934, "Italia"),
    (1938, "Italia"),
    (1950, "Uruguay"),
    (1954, "Alemaña"),
    (1958, "Brasil"),
    (1962, "Brasil"),
    (1966, "Inglaterra"),
    (1970, "Brasil"),
    (1974, "Alemaña"),
    (1978, "Argentina"),
    (1982, "Italia"),
    (1986, "Argentina"),
    (1990, "Alemaña"),
    (1994, "Brasil"),
    (1998, "Francia"),
    (2002, "Brasil"),
    (2006, "Italia"),
    (2010, "Espania"),
    (2014, "Alemaña"),
    (2018, "Francia"),
]


def contar_copas_pais(lista_copas):
    """
    Recibe una lista con el año y los ganadores de las copas del mundo
    Devuelve un dicc con los paises ganadores y la cantidad de copas ganadas
    """
    ganadores = {}
    for anio, ganador in lista_copas:
        ganadores[ganador] = ganadores.get(ganador, 0) + 1
    return ganadores


def ordenar_ganadores(dicc_ganadores):
    """
    Recibe un diccionario con la cantidad de copas ganadas por pais ganador
    Devuelve una lista ordenada con los nombres de los paises
    """
    return [
        x[0] for x in sorted(dicc_ganadores.items(), key=lambda x: x[1], reverse=True)
    ]


print(ordenar_ganadores(contar_copas_pais(copas_del_mundo)))
