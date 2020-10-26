nombres = (
    "Marhta Birnbaum",
    "Phillip Maffei",
    "Margert Haller",
    "Nia Penfield",
    "Christin Cheadle",
    "Sidney Haynes",
    "Lulu Bevan",
    "Clorinda Maire",
    "Machelle Blanton",
    "Mindi Toppin",
    "Wilma Mayne",
    "Harvey Pazos",
    "Annamarie Mattson",
    "Celena Pitre",
    "Curt Welsh",
    "Rodolfo Longfellow",
    "Ela Goetsch",
    "Reyes Lazzaro",
    "Albertine Maza",
    "Gaye Kirchner",
)

generos = (
    "hombre",
    "mujer",
    "hombre",
    "mujer",
    "otros",
    "mujer",
    "hombre",
    "mujer",
    "hombre",
    "mujer",
    "hombre",
    "mujer",
    "hombre",
    "mujer",
    "hombre",
    "mujer",
    "hombre",
    "mujer",
    "hombre",
    "mujer",
)

nombre_genero = tuple(zip(nombres, generos))


def imprimir_mensaje_electoral(nombres):
    """
    Recibe una tupla con nombre
    Imprime un mensaje con el nombre para cada uno de los nombres
    """
    for nombre in nombres:
        print(f"Estimado {nombre}, vote en mí.")


def imprimir_mensajes_inicio_cantidad(nombres, posicion_origen, cantidad):
    """
    Recibe una tupla con nombres, una posicion de origen y una cantidad
    Imprime un mensaje para los n nombres apartir de la posicion de orgine
    """
    posicion = posicion_origen
    while cantidad > 0 and posicion <= len(nombres):
        print(f"Estimado {nombres[posicion]}, vote en mí.")
        cantidad -= 1
        posicion += 1


def imprimir_mensajes_genero(nombre_genero):
    """
    Recibe una tupla de tuplas con el nombre y su genero
    """
    for persona in nombre_genero:
        final_palabra = (
            "o" if persona[1] == "hombre" else "a" if persona[1] == "mujer" else "e"
        )
        print(f"Estimad{final_palabra} {persona[0]}, vote en mi.")
