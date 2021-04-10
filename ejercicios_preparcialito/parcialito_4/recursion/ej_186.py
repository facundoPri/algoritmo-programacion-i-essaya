# Escribir una función recursiva que reciba una cadena (sin espacios), y devuelva un booleano indicando si la cadena es o no un palíndromo.


def es_polindromo(palabra):
    if len(palabra) < 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_polindromo(palabra[1:-1])
    else:
        return False


print(es_polindromo("Facundo"))
