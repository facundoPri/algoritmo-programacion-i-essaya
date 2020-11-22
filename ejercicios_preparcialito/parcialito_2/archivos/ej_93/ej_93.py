"""
Se tiene una lista de los alumnos de una materia, y se desea dividirlos en dos grupos de prácticas: grupo 1 para los alumnos con padrón impar, grupo 2 para los alumnos con padrón par.

La lista de alumnos se encuentra en un archivo en formato CSV. Se desconoce el número de columnas, pero se sabe que la primera columna es siempre el padrón, y que no hay cabecera.

Se pide escribir una función que reciba como parámetro el nombre del archivo de alumnos y escriba dos archivos, grupo1.txt y grupo2.txt, con la lista de padrones correspondientes, uno por línea.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
"""
import csv


def crear_grupos(archivo_ruta):
    """
    Recibe la ruta de un archivo que contiene una lista de alumnos en csv
    Crea dos nuevos archivos separando los alumnos por par e impar
    """
    with open(archivo_ruta) as lista_alumnos, open("grupo_1.csv", "w") as grupo_1, open(
        "grupo_2.csv", "w"
    ) as grupo_2:
        lector = csv.reader(lista_alumnos)
        grupo_1_archivo = csv.writer(grupo_1)
        grupo_2_archivo = csv.writer(grupo_2)
        for linea in lector:
            if linea[0].isdigit():
                if int(linea[0]) % 2 == 0:
                    grupo_1_archivo.writerow(linea)
                else:
                    grupo_2_archivo.writerow(linea)


crear_grupos("lista_alumnos.csv")
