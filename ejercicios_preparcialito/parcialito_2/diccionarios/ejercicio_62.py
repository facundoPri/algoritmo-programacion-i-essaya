"""
Escribir una función que reciba una cadena y devuelva un diccionario cuyas claves sean las letras y cuyos valores sean la cantidad de apariciones de dicha letra. Por ejemplo, si recibe 'catamarca' debe devolver: {'c':2, 'a':4, 't':1, 'r':1, 'm':1}.
"""


def contar_caracteres(cadena):
    """
    Recibe una cadena
    Devuelve un diccionarion con la cantidad de veces que aparece cada caracter
    """
    contador = {}
    for letra in cadena:
        contador[letra] = contador.get(letra, 0) + 1
    return contador


print(contar_caracteres("facundo"))
