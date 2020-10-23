def devolver_apenas_consonantes(cadena):
    """
    Recibe una cadena de texto
    Devuelve apenas las consonantes de esta
    """
    resultado = ""
    vocales = "aeiou"
    for letra in cadena:
        if not letra in vocales and letra == " ":
            resultado += letra
    return resultado


def devolver_apens_vocales(cadena):
    """
    Recibe una cadena de caracteres
    Devuelve apenas las vocales
    """
    resultado = ""
    vocales = "aeiou"
    for letra in cadena:
        if letra in vocales or letra == " ":
            resultado += letra
    return resultado


def devolver_siguiente_index(cadena, caracter):
    """
    Recibe una cadena de caracteres y el caracter que estamos buscando
    Devuelve de la primera vez que aparace el caracter en la cadena
    """
    for i in range(0, len(cadena)):
        if cadena[i] == caracter:
            if i == len(cadena) - 1:
                return 0
            return i + 1
    return -1


def reemplazar_vocal_por_siguiente(cadena):
    """
    Recibe una cadena de caracteres
    Reemplaza las vocales por la siguiente
    """
    resultado = ""
    vocales = "aeiou"
    for letra in cadena:
        if letra in vocales:
            resultado += vocales[devolver_siguiente_index(vocales, letra)]
        else:
            resultado += letra
    return resultado


def remover_espacios_cadena(cadena):
    """
    Recibe una cadena y de remueve los espacios
    """
    cadena_sin_espacio = ""
    for letra in cadena:
        if not letra == " ":
            cadena_sin_espacio += letra
    return cadena_sin_espacio


def es_polindromo(cadena):
    """
    Recibe una cadena de caracteres
    Devuelve True si esta cadena es un polindromo y False si no lo es
    """
    resultado = True
    cadena_sin_espacio = remover_espacios_cadena(cadena)
    tamanio_cadena = len(cadena_sin_espacio)
    for i in range(0, tamanio_cadena):
        if not cadena_sin_espacio[i] == cadena_sin_espacio[-i - 1]:
            return False
    return resultado
