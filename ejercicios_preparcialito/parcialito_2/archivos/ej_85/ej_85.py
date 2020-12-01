"""
Se tiene un archivo de texto donde cada línea es de la forma nombre_jugador,puntaje_1,puntaje_2,...,puntaje_n, representando una serie de puntajes obtenidos por un jugador (puede haber cualquier cantidad de puntajes para cada jugador, pero todos tienen al menos uno). Los puntajes no tienen decimales. Escribir un función que reciba el nombre de un archivo con la forma descripta y el nombre de un archivo destino, y escriba en él líneas de la forma nombre_jugador,puntaje_mas_alto, siendo puntaje_mas_alto el más alto de entre los puntajes de ese jugador.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
"""
import csv


def anotar_mayor_puntaje_por_jugador(ruta_archivo, archivo_final):
    """
    Recibe un archivo con el puntuaje de varios jugadores
    Crear un nuevo archivo, anotando el puntuaje mas alto de cada jugador
    """
    with open(ruta_archivo, "r") as archivo_lectura, open(
        archivo_final, "w"
    ) as archivo_resultado:
        lectura = csv.reader(archivo_lectura)
        resultado = csv.writer(archivo_resultado)
        resultado.writerow(["Nombre", "Puntuaje Max"])
        for linea in lectura:
            nombre, *puntos = linea
            max_punto = max(puntos)
            resultado.writerow([nombre, max_punto])


anotar_mayor_puntaje_por_jugador("puntuaje.txt", "resultado.txt")
