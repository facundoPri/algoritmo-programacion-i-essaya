"""
Escribir una función que reciba la ruta a un archivo de texto, y devuelva el promedio del largo de las palabras de dicho texto (considerando signos de puntuación y otros símbolos como parte de la palabra).

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
"""


def promedio_largo_palabras(ruta_archivo):
    """
    Recibe una ruta a un archivo
    Devuelve el promedio del largo de las palabras del texto
    """
    cantidad_caracteres = 0
    cantidad_palabras = 0
    with open(ruta_archivo) as texto:
        for linea in texto:
            cantidad_palabras += len(list(filter(None, linea.split(" "))))
            cantidad_caracteres += len(linea) - linea.count(" ") - linea.count("\n")
    return cantidad_caracteres / cantidad_palabras


print(promedio_largo_palabras("texto.txt"))
