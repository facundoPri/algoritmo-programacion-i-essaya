"""
Se tiene un archivo de texto que contiene un díálogo entre una cantidad de personas desconocida, de manera que cada línea del archivo tiene este formato:

PersonaN: una frase de cierta cantidad de palabras
(asumir que las frases contienen únicamente palabras, no contienen signos de puntuacion, ni numeros, ni ningun caracter que no sean letras o espacios).

Escribir una funcion que reciba la ruta a un archivo de este tipo y devuelva cuantas veces dijo cada palabra cada una de las personas involucradas en el díalogo. Es decir, debe devolver un diccionario con el siguiente formato: { persona_1: { palabra_1: cant_1, palabra_2: cant_2 }, persona_2: { ... } .. }

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
"""
import csv


def contador_palabras_chat(ruta_archivo):
    """
    Recibe un archivo representando un chat
    Devuelve un diccionarion que muesta cuantas veces dijo cada palabra cada uno de las personas
    """
    dicc = {}
    with open(ruta_archivo) as f:
        chat = csv.DictReader(
            f, fieldnames=["nombre", "mensaje"], delimiter=":", skipinitialspace=True
        )
        for linea in chat:
            nombre = linea["nombre"]
            dicc[nombre] = dicc.get(nombre, {})
            palabras = linea["mensaje"].split(" ")
            for palabra in palabras:
                dicc[nombre][palabra] = dicc[nombre].get(palabra, 0) + 1
        return dicc


print(contador_palabras_chat("dialogos.txt"))
