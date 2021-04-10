# Escribir una función recursiva que recibe una cadena s y un caracter c, y devuelve la cantidad de apariciones de c en s.


def contador_string(cadena, caracter, cantidad=0):
    if cadena == "":
        return cantidad
    if cadena[-1] == caracter:
        return contador_string(cadena[:-1], caracter, cantidad + 1)
    else:
        return contador_string(cadena[:-1], caracter, cantidad)


print(contador_string("recursion", "r"))
